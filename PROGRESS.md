# 実験進捗レポート

## 実験概要

LLMの文脈内学習（In-Context Learning）による新規プログラミング言語習得能力を、5つのシンタックスバリアントで比較する。

対象シンタックス: `yui`（日本語）, `bridget`（英語）, `wenyan`（漢文風）, `emoji`（絵文字）, `zup`（人工言語）

モデル: GPT-5.4-2026-03-05

---

## フォルダ構成

```
yuichan/
├── yui/
│   ├── humaneval/      ← yuiの164問（オリジナル）
│   └── context/        ← guide_ja.md, codesample_all.md など
├── bridget/
│   ├── data/           ← bridgetの164問（変換済み）
│   ├── context/        ← pyguide_bridget.md, ebnf_bridget.md, codesample_all_bridget.md
│   ├── templates/      ← full_context.md, zero_shot.md, one_shot.md
│   ├── results/        ← 実験結果
│   ├── evaluate.py     ← 評価スクリプト
│   └── translate_variables.py
├── wenyan/
│   ├── data/           ← wenyanの165問（全関数名・変数名・引数名漢文化済み）
│   ├── context/        ← pyguide_wenyan.md, ebnf_wenyan.md, codesample_all_wenyan.md
│   ├── templates/      ← full_context.md, zero_shot.md, one_shot.md
│   ├── results/        ← (未作成)
│   ├── evaluate.py     ← 評価スクリプト（除外問題: 19,39,84,118,149,162）
│   └── translate_variables.py  ← 変数名→漢文化スクリプト
├── emoji/              ← (未着手)
└── zup/                ← (未着手)
```

---

## bridget ✅ 完了

### データ生成

```bash
python3 -m yuichan.main --syntax yui --convert-to bridget --function-language en humaneval/*.yui
python3 bridget/translate_variables.py   # 日本語変数名→英語
```

- baseline: 97.56% (160/164)
- 残り4失敗: timeout×1, assertion×2, undefined-function×1（シンタックス問題ではない）

### 評価スクリプト

```bash
python3 bridget/evaluate.py \
  --model-name gpt-5.4-2026-03-05 \
  --template context/pyguide_bridget.md   # コンテキストファイルをそのまま渡せる
```

テンプレート解決ルール:
- `bridget/templates/` 内のファイル → ベーステンプレートとして直接使用
- それ以外（`bridget/context/*.md`）→ `full_context.md` をベースにコンテキストとして埋め込む

### データ品質修正 ✅

`--pass@1` で再測定したところ **96.95% (159/164)** となり 5 問の失敗を確認。原因を分析し修正した。

| ファイル | 原因 | 修正内容 |
|---------|------|---------|
| `36_fizz_buzz.yui` | タイムアウト | 内部ループ上限 100 → 10 |
| `39_prime_fib.yui` | タイムアウト | 素数判定に早期終了（`Leave the loop`）追加、ループ上限 10000 → 30000 |
| `149_sorted_list_sum.yui` | 結果誤り | `item j in filtered's length` が `bit j of length_integer` としてパースされる問題を中間変数で回避 |
| `19_sort_numbers.yui` | 結果誤り | 同上（`item j in words's length` のパース誤り） |
| `162_string_to_md5.yui` | 未定義関数 | ビット演算（`bitand`/`bitor`/`bitxor`/`bitnot`/`lshift`/`rshift`）を `yuistdlib.py` に追加 |

修正後: **164/164 (100%)**

なお `149_sorted_list_sum` と `19_sort_numbers` のパース問題は Yui のインデックス構文の優先順位に起因する。`item j in X's length` は `item j in (X's length)` = 整数のビット j として評価されるため、`X の要素 j の長さ` を得るには必ず中間変数を挟む必要がある。

### コンテキスト文書の作成 ✅

`bridget/context/` に以下を追加（`yui/context/` の対応ファイルを参考に、bridget 固有の仕様（反直感的な比較演算子・追記順序など）に最適化）。

| ファイル | 内容 |
|---------|------|
| `apidoc_en.md` | 標準ライブラリ API リファレンス（ビット演算セクション含む） |
| `ebnf_en.md` | 拡張 BNF 文法定義（`is at least` = `<=` 等の注意事項付き） |
| `spec_en.md` | 言語仕様書（比較演算子対応表・追記順序の注意事項を重点解説） |

### LLM実験結果（GPT-5.4, 164問）

| コンテキスト | pass@1 |
|-------------|--------|
| zero-shot   | 0.0%   |
| ebnf        | 15.85% |
| codesample  | 34.76% |
| pyguide     | 36.59% |

### 参考：日本語版（yui）の結果

| コンテキスト | pass@1 |
|-------------|--------|
| ebnf        | 6.1%   |
| codesample  | 51.83% |
| pyguide     | 54.27% |

**注目点:** bridget は ebnf で yui を上回るが、codesample・pyguide では下回る。
LLMが yui の学習データを持っている可能性あり（yui は PyPI 公開済み）。→ 後で要検討。

---

## wenyan 🔄 進行中

### やったこと

1. **全164問をwenyan形式に変換**（yui→wenyan変換は変換コマンドで実施済み）
   - `wenyan/data/` に 164問 + 164問（doctest）= 328ファイル

2. **変数名を漢文調に翻訳**（`wenyan/translate_variables.py`）
   - Claude Haiku-4.5 を使い、日本語変数名→漢文字に翻訳（49ファイル）
   - `長さ`→`長`, `結果`→`果`, `値1`→`甲`, `値2`→`乙`, `差分`→`差` など

3. **関数名・引数名・doctest も漢文化した** ✅
   - `translate_variables.py` を拡張し、main + doctest をペアで翻訳するよう変更
   - 関数名（`has_close_elements`→`近否判`）、引数名（`numbers`→`數`、`threshold`→`限`）、doctest 呼び出しも変換
   - パーサー (`yuiparser.py`) に `special-name-funcdef` / `special-name-funcparam` 抽出パターンを追加し、漢字の関数名・引数名を識別子として認識できるよう対応
   - stdlib (`yuistdlib.py`) に `餘`（剰余エイリアス）・`最大值`・`最小值`（Unicode別字エイリアス）を追加
   - **翻訳後 baseline: 96.36% (159/165)** ← 翻訳前と同値を維持

4. **翻訳後 baseline チェック** ✅
   ```bash
   python3 -m yuichan.main --pass@1 --syntax wenyan wenyan/data/*.yui
   # → 96.36% (159/165)
   ```

5. **データ品質修正** ✅

   `--pass@1` で再測定したところ **95.73% (157/164)** となり 7 問の失敗を確認。bridget と共通の問題に加え wenyan 固有の問題も修正した。

   | ファイル | 原因 | 修正内容 |
   |---------|------|---------|
   | `36_fizz_buzz.yui` | タイムアウト | 内部ループ 100 → 10 |
   | `39_prime_fib.yui` | タイムアウト | 早期終了追加、上限 10000 → 30000 |
   | `19_sort_numbers.yui` | 結果誤り | `取X之量之第j` のパース誤りを中間変数で回避 |
   | `149_sorted_list_sum.yui` | 結果誤り | 同上 |
   | `162_string_to_md5.yui` | 結果誤り | ローカル配列名 `詞` が関数引数 `詞` を上書きする問題を `訊` に改名。アキュムレータ保存/復元バグ（自己代入で保存できていなかった）も修正 |
   | `84_solve.yui` | 結果誤り | ループ内変数 `位` が配列 `位` を上書きする問題を `此位` に改名 |
   | `119_match_parens.yui` | 構文エラー | doctest 行に `>>> 施括配` プレフィックスが欠落していたのを修正 |

   修正後: **164/164 (100%)**

6. **コンテキスト文書の作成** ✅
   - `wenyan/context/codesample_all_wenyan.md`（165ファイル全収録）
   - `wenyan/context/ebnf_wenyan.md`（EBNF文法定義）
   - `wenyan/context/pyguide_wenyan.md`（Python対比形式の漢文ガイド）

7. **テンプレートの作成** ✅
   - `wenyan/templates/full_context.md`
   - `wenyan/templates/zero_shot.md`
   - `wenyan/templates/one_shot.md`（problem 0 の `近否判` 解答例を one-shot 例として使用）

8. **評価スクリプトの作成** ✅
   - `wenyan/evaluate.py`（`bridget/evaluate.py` ベース）
   - 除外問題: `EXCLUDED_PROBLEM_IDS = {19, 39, 84, 118, 149, 162}`

### ✅ 次にやること

9. **LLM実験実行**
   ```bash
   python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --no-context       # zero-shot
   python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --template context/ebnf_wenyan.md
   python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --template context/codesample_all_wenyan.md
   python3 wenyan/evaluate.py --model-name gpt-5.4-2026-03-05 --template context/pyguide_wenyan.md
   ```

### 参考: bridget との比較予測
bridget は英語構文で LLM の既存知識に近い。wenyan は漢文構文で in-context learning を純粋にテストできる。

---

## emoji 🔲 未着手

`emoji/` に 329 ファイルあり（変換済み）。wenyan 完了後に着手。

---

## zup 🔲 未着手

`zup/` に 330 ファイルあり（変換済み）。emoji 完了後に着手。
