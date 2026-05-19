#!/usr/bin/env python3
"""
Wenyan YuiEval 評価スクリプト

Usage:
    python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05
    python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --template context/codesample_all_wenyan.md
    python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --no-context
    python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --problems 0 1 2 --show-prompt

テンプレート解決ルール（bridget/evaluate.py と同仕様）:
    wenyan/templates/ 内のファイル → ベーステンプレートとして直接使用
    それ以外（wenyan/context/*.md）→ full_context.md をベースにコンテキストとして埋め込む

除外問題（ベースライン不通過）:
    19, 39, 84, 118, 149, 162
"""

import subprocess
import json
import argparse
import sys
import os
import re
import time
import tempfile
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timezone, timedelta

try:
    from dotenv import load_dotenv
    project_root = Path(__file__).resolve().parent
    env_path = project_root / '.env'
    if not env_path.exists():
        env_path = project_root.parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

SCRIPT_DIR   = Path(__file__).resolve().parent   # wenyan/
REPO_DIR     = SCRIPT_DIR.parent                  # リポジトリルート
WENYAN_DIR   = SCRIPT_DIR / 'data'
TEMPLATE_DIR = SCRIPT_DIR / 'templates'
BASE_TEMPLATE = TEMPLATE_DIR / 'full_context.md'

# ベースライン未通過のため評価から除外する問題番号
EXCLUDED_PROBLEM_IDS = {19, 39, 84, 118, 149, 162}

SYSTEM_PROMPT = "文言文（漢文）プログラミング言語 Wenyan の関数を書いてください。コンテキストをよく読んでから書いてください。"


# ── 問題ファイル処理 ──────────────────────────────────────────────────────

def extract_problem_id(path: Path) -> int:
    return int(path.stem.split('_')[0])


def find_problem_files(problems: Optional[List[str]] = None) -> List[Path]:
    all_files = sorted(
        [f for f in WENYAN_DIR.glob('*.yui')
         if not f.name.endswith('_doctest.yui') and f.stem.split('_')[0].isdigit()],
        key=extract_problem_id,
    )
    # ベースライン不通過問題を除外
    all_files = [f for f in all_files if extract_problem_id(f) not in EXCLUDED_PROBLEM_IDS]

    if problems:
        ids = set(problems)
        all_files = [f for f in all_files if str(extract_problem_id(f)) in ids]
    return all_files


def get_doctest_file(problem_file: Path) -> Optional[Path]:
    doctest = problem_file.parent / (problem_file.stem + '_doctest.yui')
    return doctest if doctest.exists() else None


def parse_wenyan_file(filepath: Path) -> Dict:
    """wenyan .yui ファイルから関数名・ヘッダー・doctestを抽出する"""
    code = filepath.read_text(encoding='utf-8')
    lines = code.splitlines()

    has_stdlib = any('引標準庫' in l for l in lines)

    # 関数名・引数を 術曰funcname以param1與param2 から抽出
    func_name = ''
    func_args = []
    header_line = ''
    for line in lines:
        m = re.match(r'術曰\s*(\S+?)(?:\s*以\s*(.+))?$', line.strip())
        if m:
            func_name = m.group(1)
            args_str = m.group(2) or ''
            func_args = [a.strip() for a in re.split(r'與', args_str) if a.strip()]
            header_line = line.strip()
            break

    # doctest行の抽出
    doctests = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('>>>'):
            expr = lines[i].strip()
            expected = lines[i + 1].strip() if i + 1 < len(lines) else ''
            doctests.append((expr, expected))
            i += 2
        else:
            i += 1

    header_block = ('引標準庫\n' if has_stdlib else '') + header_line

    return {
        'func_name': func_name,
        'func_args': func_args,
        'func_header': header_block,
        'doctests': doctests,
    }


def make_problem_text(problem: Dict, num_examples: int = 3) -> str:
    """プロンプトに埋め込む問題文を生成する"""
    example_lines = []
    for expr, expected in problem['doctests'][:num_examples]:
        example_lines.append(expr)
        example_lines.append(expected)

    return (
        f"以下の Wenyan 関数を完成させてください:\n\n"
        f"{problem['func_header']}\n\n"
        f"期待される動作:\n" + '\n'.join(example_lines)
    )


# ── テンプレート処理 ──────────────────────────────────────────────────────

def create_prompt_from_template(template_path: Path, problem_text: str,
                                context_file: Optional[Path] = None,
                                no_context: bool = False) -> str:
    tpath = template_path.resolve()

    if tpath.parent == TEMPLATE_DIR.resolve():
        template = tpath.read_text(encoding='utf-8')
        if no_context or context_file is None:
            context_text = ''
        else:
            if not context_file.exists():
                print(f"Warning: context file not found: {context_file}", file=sys.stderr)
                context_text = ''
            else:
                context_text = context_file.read_text(encoding='utf-8')
        prompt = template.replace('{CONTEXT}', context_text)
    else:
        base = BASE_TEMPLATE.read_text(encoding='utf-8')
        context_text = tpath.read_text(encoding='utf-8')
        prompt = base.replace('{CONTEXT}', context_text)

    return prompt.replace('{PROBLEM}', problem_text)


# ── コード抽出 ────────────────────────────────────────────────────────────

def extract_wenyan_code(generated: str, func_name: str) -> str:
    """LLM の出力から wenyan コードを抽出する"""
    if not generated:
        return ''

    text = generated.strip()

    # ```wenyan ... ``` または ``` ... ``` ブロック
    m = re.search(r'```(?:wenyan)?\s*\n(.*?)```', text, re.DOTALL)
    if m:
        code = m.group(1).strip()
        if '引標準庫' not in code and func_name:
            return '引標準庫\n' + code
        return code

    # 術曰funcname ... 術畢 ブロック
    if func_name:
        pattern = rf'(?:引標準庫\n)?術曰\s*{re.escape(func_name)}.*?術畢'
        m = re.search(pattern, text, re.DOTALL)
        if m:
            block = m.group(0)
            if '引標準庫' not in block:
                return '引標準庫\n' + block
            return block

    return text


# ── 評価 ─────────────────────────────────────────────────────────────────

def test_generated_code(generated_code: str, doctest_path: Path, timeout: int = 30) -> Tuple[bool, str, str, float]:
    if not generated_code:
        return False, '', 'Empty code', 0.0

    start = time.time()
    try:
        doctest_code = doctest_path.read_text(encoding='utf-8') if doctest_path else ''
        full_code = generated_code.rstrip() + '\n' + doctest_code

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yui', delete=False, encoding='utf-8') as f:
            f.write(full_code)
            tmp_path = f.name

        try:
            result = subprocess.run(
                [sys.executable, '-m', 'yuichan.main', '--syntax', 'wenyan', tmp_path],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(REPO_DIR),
            )
            elapsed = time.time() - start
            success = result.returncode == 0
            stderr = (result.stderr or result.stdout).strip()
            return success, result.stdout, stderr, elapsed
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    except subprocess.TimeoutExpired:
        return False, '', f'Timeout ({timeout}s)', time.time() - start
    except Exception as e:
        return False, '', str(e), time.time() - start


# ── API 呼び出し ──────────────────────────────────────────────────────────

def detect_provider(model_name: str) -> str:
    lo = model_name.lower()
    if lo.startswith('gpt') or lo.startswith('o1') or lo.startswith('o3') or lo.startswith('o4'):
        return 'openai'
    if lo.startswith('claude'):
        return 'anthropic'
    if lo.startswith('mlx-community/') or lo.startswith('mlx/'):
        return 'mlx'
    if '/' in model_name:
        return 'huggingface'
    return 'ollama'


def wilson_confidence_interval(passed: int, total: int, confidence: float = 0.95):
    from math import sqrt
    if total == 0:
        return 0.0, 0.0
    z = 1.96 if confidence == 0.95 else 2.576
    p = passed / total
    n = total
    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    margin = z * sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


def call_openai_api(system_prompt, user_prompt, api_key, model_name, temperature=0.2, k=1):
    try:
        import openai
    except ImportError:
        print("Error: pip install openai", file=sys.stderr); sys.exit(1)

    client = openai.OpenAI(api_key=api_key)
    try:
        use_new = any(x in model_name.lower() for x in ['gpt-5', 'o1', 'o3', 'o4'])
        kwargs = dict(
            model=model_name,
            messages=[{'role': 'system', 'content': system_prompt},
                      {'role': 'user',   'content': user_prompt}],
            n=k,
        )
        if use_new:
            kwargs['max_completion_tokens'] = 2000
            if not any(x in model_name.lower() for x in ['o1', 'o3', 'o4']):
                kwargs['temperature'] = temperature
        else:
            kwargs['max_tokens'] = 2000
            kwargs['temperature'] = temperature

        response = client.chat.completions.create(**kwargs)
        return [c.message.content for c in response.choices]
    except Exception as e:
        print(f"  OpenAI error: {e}", file=sys.stderr)
        return [None] * k


def call_anthropic_api(system_prompt, user_prompt, api_key, model_name, temperature=0.2, k=1):
    try:
        import anthropic
    except ImportError:
        print("Error: pip install anthropic", file=sys.stderr); sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    results = []
    for _ in range(k):
        try:
            response = client.messages.create(
                model=model_name,
                max_tokens=2000,
                temperature=temperature,
                system=system_prompt,
                messages=[{'role': 'user', 'content': user_prompt}],
            )
            results.append(response.content[0].text)
        except Exception as e:
            print(f"  Anthropic error: {e}", file=sys.stderr)
            results.append(None)
    return results


def call_ollama_api(system_prompt, user_prompt, model_name, temperature=0.2, k=1):
    try:
        import requests
    except ImportError:
        print("Error: pip install requests", file=sys.stderr); sys.exit(1)

    results = []
    for _ in range(k):
        try:
            resp = requests.post(
                'http://localhost:11434/api/chat',
                json={
                    'model': model_name,
                    'messages': [{'role': 'system', 'content': system_prompt},
                                 {'role': 'user',   'content': user_prompt}],
                    'stream': False,
                    'options': {'temperature': temperature, 'num_predict': 2000},
                },
            )
            results.append(resp.json()['message']['content'])
        except Exception as e:
            print(f"  Ollama error: {e}", file=sys.stderr)
            results.append(None)
    return results


# ── メイン ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Wenyan YuiEval 評価スクリプト')
    parser.add_argument('--model', default=None,
                        choices=['openai', 'anthropic', 'ollama', 'huggingface', 'mlx'])
    parser.add_argument('--model-name', default=None,
                        help='モデル名 (e.g. gpt-5.4-2026-03-05, claude-haiku-4-5-20251001)')
    parser.add_argument('--api-key', default=None)
    parser.add_argument('--temperature', type=float, default=0.2)
    parser.add_argument('--k', type=int, default=1)
    parser.add_argument('--template', default='templates/full_context.md',
                        help='テンプレートまたはコンテキストファイル')
    parser.add_argument('--context-file', default=None)
    parser.add_argument('--no-context', action='store_true')
    parser.add_argument('--num-examples', type=int, default=3)
    parser.add_argument('--problems', nargs='*', default=None,
                        help='評価する問題番号 (e.g. 0 1 5)。省略時は除外問題を除く全問題')
    parser.add_argument('--timeout', type=int, default=30)
    parser.add_argument('--output-dir', default=str(SCRIPT_DIR / 'results'))
    parser.add_argument('--show-prompt', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    if not args.model and not args.show_prompt:
        if args.model_name:
            args.model = detect_provider(args.model_name)
            print(f"自動判別: {args.model_name} → {args.model}")
        else:
            print("Error: --model または --model-name を指定してください", file=sys.stderr)
            return 1

    template_path = Path(args.template)
    if not template_path.is_absolute():
        template_path = SCRIPT_DIR / args.template
    if not template_path.exists():
        print(f"Error: テンプレートが見つかりません: {template_path}", file=sys.stderr)
        return 1

    context_file = None
    if args.context_file:
        context_file = Path(args.context_file)
        if not context_file.is_absolute():
            context_file = SCRIPT_DIR / args.context_file
        if not context_file.exists():
            print(f"Error: コンテキストファイルが見つかりません: {context_file}", file=sys.stderr)
            return 1

    is_base_template = template_path.resolve().parent == TEMPLATE_DIR.resolve()
    if args.no_context:
        context_label = 'none'
    elif is_base_template:
        context_label = context_file.name if context_file else 'none'
    else:
        context_label = template_path.name

    if args.show_prompt:
        files = find_problem_files(args.problems)
        if not files:
            print("Error: 問題ファイルが見つかりません", file=sys.stderr)
            return 1
        problem = parse_wenyan_file(files[0])
        problem_text = make_problem_text(problem, args.num_examples)
        user_prompt = create_prompt_from_template(template_path, problem_text,
                                                  context_file=context_file,
                                                  no_context=args.no_context)
        print(f"=== プロンプトプレビュー ===")
        print(f"問題: {files[0].name}")
        print(f"テンプレート: {args.template}")
        print(f"コンテキスト: {context_label}")
        print()
        print("--- System Prompt ---")
        print(SYSTEM_PROMPT)
        print()
        print("--- User Prompt ---")
        print(user_prompt[:3000])
        if len(user_prompt) > 3000:
            print(f"\n... ({len(user_prompt)} chars total)")
        return 0

    api_key = None
    model_name = args.model_name
    if args.model == 'openai':
        api_key = args.api_key or os.getenv('OPENAI_API_KEY')
        model_name = model_name or 'gpt-4'
        if not api_key:
            print("Error: OPENAI_API_KEY が設定されていません", file=sys.stderr)
            return 1
    elif args.model == 'anthropic':
        api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
        model_name = model_name or 'claude-3-5-sonnet-20241022'
        if not api_key:
            print("Error: ANTHROPIC_API_KEY が設定されていません", file=sys.stderr)
            return 1
    else:
        model_name = model_name or 'codellama'

    problem_files = find_problem_files(args.problems)
    if not problem_files:
        print("Error: 問題ファイルが見つかりません", file=sys.stderr)
        return 1

    jst = timezone(timedelta(hours=9))
    ts = datetime.now(jst).strftime('%Y%m%d_%H%M%S')
    safe_model = model_name.replace('/', '_').replace(':', '_')
    template_tag = template_path.stem
    out_dir = Path(args.output_dir) / f"{ts}_{safe_model}_{template_tag}"
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = out_dir / 'generated'
    generated_dir.mkdir(exist_ok=True)

    log_path = out_dir / 'log.txt'
    log_handle = open(log_path, 'w', encoding='utf-8')

    def log(msg: str):
        print(msg)
        log_handle.write(msg + '\n')
        log_handle.flush()

    log(f"=== Wenyan YuiEval (pass@{args.k}) ===")
    log(f"Model:    {model_name}  ({args.model})")
    log(f"Template: {args.template}")
    log(f"Context:  {context_label}")
    log(f"Problems: {len(problem_files)} (除外: {sorted(EXCLUDED_PROBLEM_IDS)})")
    log("")

    all_results = []
    results_by_problem = {}

    for idx, filepath in enumerate(problem_files, 1):
        problem_id = str(extract_problem_id(filepath))
        problem_name = filepath.stem
        start_time = time.time()

        log(f"[{idx}/{len(problem_files)}] {problem_name}")

        problem = parse_wenyan_file(filepath)
        doctest_file = get_doctest_file(filepath)

        if not doctest_file:
            log(f"  Warning: doctest file not found, skipping")
            continue

        problem_text = make_problem_text(problem, args.num_examples)
        user_prompt = create_prompt_from_template(template_path, problem_text,
                                                  context_file=context_file,
                                                  no_context=args.no_context)

        if args.model == 'openai':
            generated_codes = call_openai_api(SYSTEM_PROMPT, user_prompt, api_key, model_name, args.temperature, args.k)
        elif args.model == 'anthropic':
            generated_codes = call_anthropic_api(SYSTEM_PROMPT, user_prompt, api_key, model_name, args.temperature, args.k)
        else:
            generated_codes = call_ollama_api(SYSTEM_PROMPT, user_prompt, model_name, args.temperature, args.k)

        canonical_solution = filepath.read_text(encoding='utf-8')

        samples_passed = 0
        if problem_id not in results_by_problem:
            results_by_problem[problem_id] = []

        for j, generated in enumerate(generated_codes):
            extracted = extract_wenyan_code(generated or '', problem['func_name'])

            if extracted:
                code_file = generated_dir / f"{problem_name}_sample_{j}.yui"
                code_file.write_text(extracted, encoding='utf-8')

            log_handle.write(f"\n{'='*60}\n[{problem_name}] Sample {j+1}/{args.k}\n{'='*60}\n")
            log_handle.write(f"--- Generated ---\n{generated}\n")
            log_handle.write(f"--- Extracted ---\n{extracted}\n")
            log_handle.flush()

            success, stdout, stderr, elapsed = test_generated_code(extracted, doctest_file, args.timeout)

            if success:
                log(f"  Sample {j+1}/{args.k}... ✓ ({elapsed:.2f}s)")
                log_handle.write(f"--- Result: ✓ PASSED ({elapsed:.2f}s) ---\n")
                samples_passed += 1
            else:
                log(f"  Sample {j+1}/{args.k}... ✗ ({elapsed:.2f}s)")
                log_handle.write(f"--- Result: ✗ FAILED ({elapsed:.2f}s) ---\nError: {stderr}\n")
                if args.verbose and stderr:
                    log(f"    Error: {stderr[:200]}")

            results_by_problem[problem_id].append(success)
            all_results.append({
                'problem_id': problem_id,
                'problem_name': problem_name,
                'sample_id': j,
                'model': model_name,
                'canonical_solution': canonical_solution,
                'input': SYSTEM_PROMPT + '\n\n' + user_prompt,
                'output': generated,
                'extracted': extracted,
                'passed': success,
                'error': stderr if not success else None,
                'execution_time': elapsed,
            })

        problem_elapsed = time.time() - start_time
        passed_this = any(results_by_problem[problem_id])
        status = '✓' if passed_this else '✗'
        log(f"  Problem result: {status} ({samples_passed}/{args.k} passed) [{problem_elapsed:.2f}s]")
        log("")

    total = len(results_by_problem)
    passed = sum(1 for r in results_by_problem.values() if any(r))
    failed = total - passed
    pass_rate = passed / total * 100 if total > 0 else 0.0
    ci_lower, ci_upper = wilson_confidence_interval(passed, total)

    log("=" * 60)
    log("評価結果サマリー")
    log("=" * 60)
    log(f"Total:   {total} 問題")
    log(f"Passed:  {passed} 問題")
    log(f"Failed:  {failed} 問題")
    log(f"pass@{args.k}: {pass_rate:.2f}% ({passed}/{total})")
    log(f"95% CI: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%] (Wilson Score)")

    if failed > 0:
        log("\n失敗した問題:")
        for r in all_results:
            if not r['passed'] and r['sample_id'] == 0:
                if not any(results_by_problem.get(r['problem_id'], [])):
                    log(f"  - {r['problem_name']}")

    result_file = out_dir / 'result.jsonl'
    with open(result_file, 'w', encoding='utf-8') as f:
        for r in all_results:
            json.dump(r, f, ensure_ascii=False)
            f.write('\n')

    summary = {
        'model': model_name,
        'template': args.template,
        'context': context_label,
        'temperature': args.temperature,
        'k': args.k,
        'total_problems': total,
        'passed_problems': passed,
        'failed_problems': failed,
        'pass_at_k': round(pass_rate, 2),
        'confidence_interval_95': {
            'lower': round(ci_lower * 100, 2),
            'upper': round(ci_upper * 100, 2),
            'method': 'Wilson Score',
        },
        'excluded_problem_ids': sorted(EXCLUDED_PROBLEM_IDS),
        'timestamp': ts,
        'total_samples': len(all_results),
        'passed_samples': sum(1 for r in all_results if r['passed']),
    }
    summary_file = out_dir / 'summary.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    log(f"\n生成コード: {generated_dir}")
    log(f"詳細結果:   {result_file}")
    log(f"サマリー:   {summary_file}")
    log(f"ログ:       {log_path}")
    log_handle.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
