#!/usr/bin/env python3
"""
bridget/*.yui の日本語変数名を英語に翻訳するスクリプト。

使い方:
  python3 translate_variables.py [--dry-run] [files...]
  python3 translate_variables.py bridget/0_has_close_elements.yui   # 1ファイル
  python3 translate_variables.py                                     # 全ファイル
"""

import anthropic
import sys
import glob
import time
from pathlib import Path

SYSTEM_PROMPT = """\
You are a code translator. Your task is to translate Japanese variable names and parameter names in Yui language (bridget syntax) to English.

Rules:
1. Translate ONLY Japanese variable names and function parameter names to short, clear English names
2. Keep ALL bridget syntax keywords unchanged: Remember that, Do this, When, End when, End do, The answer is, This is how to, Now you know, Use the standard library, Increase, Decrease, Add, Leave the loop, etc.
3. Keep ALL English stdlib function names unchanged: sum, diff, product, remainder, abs, max, min, quotient, sqrt, isint, isfloat, isstring, isarray, isobject, toint, tofloat, tostring, toarray, isbool, random
4. Keep ALL function names after "This is how to" unchanged
5. Keep ALL doctest lines unchanged (lines starting with >>> or containing only expected output values)
6. Keep ALL string literals, numbers, and array contents unchanged
7. Translate consistently: use the same English name everywhere a Japanese name appears
8. Single-letter variables (i, j, k, n, x, y, z) can stay as-is
9. Return ONLY the translated code with no explanation or markdown

Common translations:
- 結果 → result
- 長さ → length
- 値 → value
- 合計 → total
- 差分 → delta
- 絶対差分 → abs_delta
- 上限 → limit
- 下限 → lower
- 余り → remainder_val (avoid conflict with stdlib 'remainder')
- カウント → count
- フラグ → flag
- 文字 → char
- 文字列 → string_val
- 配列 → arr
- インデックス → idx
- 最大 → maximum
- 最小 → minimum
"""

USER_PROMPT_TEMPLATE = """\
Translate the Japanese variable names in this bridget-syntax Yui code to English:

{code}
"""


def translate_file(client: anthropic.Anthropic, path: Path, dry_run: bool = False) -> bool:
    code = path.read_text(encoding="utf-8")

    # 日本語識別子がなければスキップ
    if not any(ord(c) > 0x7F for c in code):
        print(f"  skip (no Japanese): {path.name}")
        return False

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(code=code)}
        ],
    )

    translated = response.content[0].text.strip()

    # コードブロックが含まれていたら中身だけ取る
    if translated.startswith("```"):
        lines = translated.split("\n")
        translated = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    if dry_run:
        print(f"\n{'='*60}")
        print(f"FILE: {path}")
        print(f"{'='*60}")
        print(translated[:500])
        return True

    path.write_text(translated + "\n", encoding="utf-8")
    print(f"  translated: {path.name}")
    return True


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]

    if args:
        files = [Path(a) for a in args]
    else:
        files = sorted(Path("bridget").glob("*.yui"))
        files = [f for f in files if "_doctest" not in f.name]

    client = anthropic.Anthropic()

    print(f"Translating {len(files)} files{'  [DRY RUN]' if dry_run else ''}...")
    changed = 0
    for i, path in enumerate(files):
        try:
            if translate_file(client, path, dry_run=dry_run):
                changed += 1
            if i % 10 == 9:
                time.sleep(1)  # レートリミット対策
        except Exception as e:
            print(f"  ERROR {path.name}: {e}")

    print(f"\nDone: {changed}/{len(files)} files translated.")


if __name__ == "__main__":
    main()
