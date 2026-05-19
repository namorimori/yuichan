#!/usr/bin/env python3
"""
wenyan/data/*.yui の日本語変数名・英語関数名・英語引数名を漢文調の漢字に翻訳するスクリプト。
main ファイルと対応する _doctest ファイルをペアで処理し、一貫した翻訳を保証する。

使い方:
  python3 wenyan/translate_variables.py [--dry-run] [files...]
  python3 wenyan/translate_variables.py wenyan/data/0_has_close_elements.yui
  python3 wenyan/translate_variables.py                  # 全ファイル
"""
from __future__ import annotations

import anthropic
import sys
import time
from pathlib import Path

SYSTEM_PROMPT = """\
You are a classical Chinese (文言文) code translator. Your task is to translate Wenyan-style Yui language code into fully classical Chinese style by:
1. Translating Japanese variable names (hiragana/katakana/Japanese kanji used as variable names) to short classical Chinese characters
2. Translating English function names (snake_case) to concise classical Chinese (2-3 characters)
3. Translating English parameter names to classical Chinese (1-2 characters)
4. Updating ALL >>> doctest lines to use the new Chinese function/parameter names

Rules:
- Keep ALL wenyan syntax keywords unchanged: 引標準庫、術曰、以、與、吾有一數、曰、名之曰、若、乎、則、條畢、度、度畢、術畢、增...以一、減...以一、納...入、以...答、還無、施...於、之量、之第、取、引、etc.
- Keep ALL stdlib function names unchanged: 和、差、積、商、餘、絶対値、最大値、最小値、長さ (when used as stdlib calls)
- Keep ALL string literals 「...」, numbers, and array contents unchanged
- Single-letter ASCII variables (i, j, k, n, x, y, z) stay as-is
- Translate consistently: same name → same translation throughout ALL files
- Return ONLY the translated code with no explanation or markdown

Function name translation guidelines:
- 2-3 character classical Chinese, describing the function's purpose
- Examples: has_close_elements → 近否判, make_palindrome → 迴文造, string_xor → 弦互異

Parameter name translation guidelines:
- 1-2 character classical Chinese
- Examples: numbers → 數, threshold → 限, string → 詞, lst → 列, n → n

Classical Chinese variable name guidelines:
- 甲乙丙丁 for enumerated values
- 上下左右前後 for positional concepts

Common variable translations:
- 長さ (as variable) → 長
- 結果 → 果  (※ 答 は return キーワードと衝突)
- 値1、一値 → 甲
- 値2、二値 → 乙
- 差分 → 差
- 絶対差分 → 距
- カウント、数 → 計
- フラグ → 標
- 最大 → 極
- 最小 → 微
- 合計 → 總
- インデックス → 位
- 文字 → 字
- 文字列 → 詞
- 配列 → 列
- 余り → 餘
- 上限 → 限
- 下限 → 下
- 素数 → 素
- 逆 → 逆
- 桁 → 桁
- 一時 → 暫
- 現在 → 今
- 次 → 次
- 前 → 前
- 後 → 後
- 左 → 左
- 右 → 右
- 幅 → 幅
- 深さ → 深
- 高さ → 高
- 重み → 重
- 候補 → 候
- 部分 → 部
- 要素 → 元
- 境界 → 界
"""

USER_PROMPT_TEMPLATE_PAIR = """\
Translate this Wenyan-style Yui code. Apply consistent translations to BOTH files.

=== MAIN FILE ===
{main_code}

=== DOCTEST FILE ===
{doctest_code}

Return in EXACTLY this format (keep the === markers):
=== MAIN FILE ===
[translated main code]

=== DOCTEST FILE ===
[translated doctest code]
"""

USER_PROMPT_TEMPLATE_SINGLE = """\
Translate this Wenyan-style Yui code to fully classical Chinese style:

{code}
"""


def has_english_identifiers(text: str) -> bool:
    """英語の識別子（関数名・引数名）が含まれているか確認"""
    import re
    # 術曰xxx（関数定義）または 施xxx於（関数呼び出し）に英字があれば True
    return bool(re.search(r'術曰[a-zA-Z_]|施[a-zA-Z_]', text))


def has_japanese(text: str) -> bool:
    for c in text:
        cp = ord(c)
        if 0x3040 <= cp <= 0x30FF:  # ひらがな・カタカナ
            return True
        if 0xFF01 <= cp <= 0xFF9F:  # 全角英数・半角カタカナ
            return True
    return False


def needs_translation(text: str) -> bool:
    return has_japanese(text) or has_english_identifiers(text)


def parse_pair_response(response: str) -> tuple[str, str]:
    """=== MAIN FILE === / === DOCTEST FILE === で分割して (main, doctest) を返す"""
    main_marker = "=== MAIN FILE ==="
    doctest_marker = "=== DOCTEST FILE ==="

    main_start = response.find(main_marker)
    doctest_start = response.find(doctest_marker)

    if main_start == -1 or doctest_start == -1:
        raise ValueError(f"Expected markers not found in response:\n{response[:300]}")

    main_code = response[main_start + len(main_marker):doctest_start].strip()
    doctest_code = response[doctest_start + len(doctest_marker):].strip()

    return main_code, doctest_code


def strip_code_fence(text: str) -> str:
    if text.startswith("```"):
        lines = text.split("\n")
        end = -1 if lines[-1].strip() == "```" else len(lines)
        return "\n".join(lines[1:end])
    return text


def translate_pair(
    client: anthropic.Anthropic,
    main_path: Path,
    doctest_path: Path | None,
    dry_run: bool = False,
) -> bool:
    main_code = main_path.read_text(encoding="utf-8")
    doctest_code = doctest_path.read_text(encoding="utf-8") if doctest_path and doctest_path.exists() else None

    if not needs_translation(main_code) and (doctest_code is None or not needs_translation(doctest_code)):
        print(f"  skip (nothing to translate): {main_path.name}")
        return False

    if doctest_code is not None:
        prompt = USER_PROMPT_TEMPLATE_PAIR.format(
            main_code=main_code,
            doctest_code=doctest_code,
        )
    else:
        prompt = USER_PROMPT_TEMPLATE_SINGLE.format(code=main_code)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()

    if doctest_code is not None:
        try:
            translated_main, translated_doctest = parse_pair_response(raw)
        except ValueError:
            # フォールバック: 全体を main として扱う
            print(f"  WARN: failed to parse pair response for {main_path.name}, using raw as main")
            translated_main = strip_code_fence(raw)
            translated_doctest = None
    else:
        translated_main = strip_code_fence(raw)
        translated_doctest = None

    if dry_run:
        print(f"\n{'='*60}")
        print(f"FILE: {main_path.name}")
        print(f"{'='*60}")
        print(translated_main[:600])
        if translated_doctest:
            print(f"\n--- DOCTEST ---")
            print(translated_doctest[:300])
        return True

    main_path.write_text(translated_main + "\n", encoding="utf-8")
    print(f"  translated: {main_path.name}")

    if translated_doctest and doctest_path:
        doctest_path.write_text(translated_doctest + "\n", encoding="utf-8")
        print(f"  translated: {doctest_path.name}")

    return True


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]

    script_dir = Path(__file__).resolve().parent

    if args:
        # 指定ファイルから main ファイルのみ抽出し、ペアで処理
        main_files = [Path(a) for a in args if "_doctest" not in Path(a).name]
    else:
        main_files = sorted((script_dir / "data").glob("*.yui"))
        main_files = [f for f in main_files if "_doctest" not in f.name]

    client = anthropic.Anthropic()

    print(f"Translating {len(main_files)} file pairs to 漢文調{'  [DRY RUN]' if dry_run else ''}...")
    changed = 0
    for i, main_path in enumerate(main_files):
        stem = main_path.stem  # e.g. "0_has_close_elements"
        doctest_path = main_path.parent / f"{stem}_doctest.yui"
        if not doctest_path.exists():
            doctest_path = None

        try:
            if translate_pair(client, main_path, doctest_path, dry_run=dry_run):
                changed += 1
            if i % 10 == 9:
                time.sleep(1)
        except Exception as e:
            print(f"  ERROR {main_path.name}: {e}")

    print(f"\nDone: {changed}/{len(main_files)} file pairs translated.")


if __name__ == "__main__":
    main()
