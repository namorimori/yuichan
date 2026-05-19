# CONTEXT.md — 文脈内学習コンテキストファイル概要

## 1. 概要

本プロジェクトでは、同一の Yui ランタイム上に実装された 3 つの構文方言 **yui（日本語）**・**bridget（英語）**・**wenyan（文言文）** を対象に、LLM の文脈内学習（in-context learning）効果を比較実験する。各シンタックスごとにコンテキストファイル群を用意し、1 ファイルずつ独立して LLM に与えることで、シンタックスの言語圏と文脈の与え方が HumanEval ベンチマーク上の Pass@1 に与える影響を測定する。

---

## 2. シンタックス概要

| シンタックス | 言語 | 特徴 |
|---|---|---|
| **yui** | 日本語 | 日本語のキーワード・変数名。自然な日本語語順。記号を最小化。 |
| **bridget** | 英語 | 英語キーワードで数学記号を排除。構造化英語命令形式。 |
| **wenyan** | 文言文 | 古典中国語（漢文）のキーワード・変数名。漢字のみで記述。 |

3 シンタックスは同一ランタイムを共有し、同等の機能を持つ。制御フロー・型システム・標準ライブラリは対応している。

---

## 3. コンテキストファイル構成

各シンタックスのコンテキストファイルは `<syntax>/context/` ディレクトリに格納される。

### 3.1 ファイル一覧と行数

| ファイル名 | yui | bridget | wenyan | 内容 |
|---|---|---|---|---|
| spec | spec_en.md (267行) | spec_en.md (308行) | spec_zh.md (325行) | 言語仕様 |
| ebnf | ebnf_en.md (246行) | ebnf_en.md (268行) | ebnf_zh.md (262行) | EBNF 文法定義 |
| guide | guide_en.md (642行) | guide_en.md (678行) | guide_zh.md (706行) | プログラミングガイド |
| apidoc | apidoc_en.md (221行) | apidoc_en.md (195行) | apidoc_zh.md (225行) | 標準ライブラリ API リファレンス |
| pyguide | pyguide_en.md (698行) | pyguide_en.md (810行) | pyguide_zh.md (781行) | Python 対比学習ガイド |
| example_11 | example_11.md (590行) | example_11.md (306行) | example_11.md (501行) | 言語最適化コード例 11 ブロック |
| example_11_translated | — | example_11_translated.md (575行) | example_11_translated.md (578行) | yui/example_11 の直接翻訳版 |
| example_33 | example_33.md (1808行) | example_33_translated.md (1618行) | example_33_translated.md (1780行) | アルゴリズム例 33 ブロック |

yui は参照言語のため `example_11_translated` は存在しない。

---

## 4. ファイルの種別と目的

### 4.1 言語仕様・文法ファイル（spec / ebnf）

- `spec`: 型システム・制御フロー・演算子など言語仕様をナチュラルランゲージで記述。
- `ebnf`: 構文を Extended BNF で形式定義。パーサーの参照仕様として機能する。

### 4.2 学習ガイド（guide / pyguide）

- `guide`: 各言語機能を段階的に解説するプログラミングガイド。
- `pyguide`: Python コードと対比する形で各機能を説明する Python ユーザー向けガイド。各機能を「Python 版 → 当該シンタックス版」の対比形式で示す。

### 4.3 コード例（example_11 / example_11_translated / example_33）

コード例ファイルは、コードブロックと `>>>` doctest スタイルの期待値をセットで記述する形式を採用している。LLM はこれを見本として同形式で HumanEval 問題を解く。

#### example_11

各シンタックスの言語的特徴を示す 11 ブロックのコード例。各ブロックは実行可能なコードと doctest を含む。

| ブロック | 内容 |
|---|---|
| 1 | スタックマシン（`push`/`pop`/`add`/`mul`/`neg` 命令） |
| 2 | 成績判定（A/B/C/D/F の多段分岐） |
| 3 | 複数値返却（配列・オブジェクトの 2 通り） |
| 4 | 複利計算 |
| 5 | 文字列補間・引数なし関数 |
| 6 | 集合の所属判定（含む・含まない） |
| 7 | 無操作（no-op）のデモ |
| 8 | サイコロシミュレーション（乱数・配列） |
| 9 | ROT13 |
| 10 | 型判定関数 6 種 |
| 11 | 可変長引数・無引数呼び出し・括弧式 |

**example_11 のファイル対応関係：**

- `yui/context/example_11.md`：yui 向けに最適化した原版
- `bridget/context/example_11_translated.md`：上記の bridget 直接翻訳版
- `wenyan/context/example_11_translated.md`：上記の wenyan 直接翻訳版
- `bridget/context/example_11.md`：bridget 向けに言語最適化した版
- `wenyan/context/example_11.md`：wenyan 向けに言語最適化した版

#### example_33

HumanEval と重複しない問題を人手で作成した 33 件のコード例。各ブロックは独立したアルゴリズム実装と doctest で構成される。

| # | 関数名（yui）| 内容 |
|---|---|---|
| 1 | bin_to_int | 2 進数文字列→整数変換 |
| 2 | bits_add | ビット加算（1 ビット全加算器） |
| 3 | bits_and / bits_or / bits_xor | ビット論理演算（AND / OR / XOR） |
| 4 | lshift / rshift | 整数ビットシフト |
| 5 | bmi_category | BMI 分類（早期 return パターン） |
| 6 | bubble_sort | バブルソート |
| 7 | closest | 配列中の最近値探索 |
| 8 | compound / years_to_double | 複利計算・倍化年数 |
| 9 | count_vowels / first_vowel | 母音カウント・最初の母音位置 |
| 10 | count_dice | サイコロ N 回のヒストグラム |
| 11 | distance | 2 点間ユークリッド距離 |
| 12 | dot | ベクトル内積 |
| 13 | grade / passed | 点数→成績変換・合否判定 |
| 14 | motto / greet / score_msg | 文字列補間・引数なし関数デモ |
| 15 | leap_year | うるう年判定 |
| 16 | leibniz | ライプニッツ公式による π 近似 |
| 17 | minor / det | 行列式（ラプラス展開） |
| 18 | max / min / clamp | 最大値・最小値・クランプ |
| 19 | menu / check / allergy / safe | 集合所属検索（含む・含まない） |
| 20 | divmod_array / stats / point | 複数値返却（配列・オブジェクト） |
| 21 | sign | 何もしない（no-op）のデモ・符号関数 |
| 22 | solve | 二次方程式の実数解 |
| 23 | walk | 1 次元ランダムウォーク |
| 24 | reverse | 配列反転 |
| 25 | rot13 | ROT13 古典暗号 |
| 26 | count_pass_v1 / count_pass_v2 | 無効値を除いた合格者カウント（2 実装） |
| 27 | run | 簡易スタックマシン |
| 28 | find | 部分文字列の位置検索 |
| 29 | replace | 文字列の全置換 |
| 30 | to_str / digits | 文字列化・桁数計算 |
| 31 | classify | 三角形分類（3 辺） |
| 32 | (型判定群) | 6 種の型判定関数と null |
| 33 | unique_chars | 文字列からユニーク文字抽出 |

---

## 5. 実験設計

### 5.1 文脈内学習の方式

LLM には 1 度に 1 つの markdown ファイルのみを提供する（複数ファイルの同時付与は行わない）。各ファイル単体が完結したコンテキストとして機能するよう設計されている。

### 5.2 比較実験（主実験）

3 シンタックス間の直接比較は、同一コンテンツの直接翻訳ファイルを用いる。

| シンタックス | 使用ファイル |
|---|---|
| yui | `yui/context/example_11.md` |
| bridget | `bridget/context/example_11_translated.md` |
| wenyan | `wenyan/context/example_11_translated.md` |

この 3 ファイルは同一のコード構造・同一のアルゴリズムを持ち、シンタックスのみ異なる。これにより、コンテンツの差異を排除したシンタックス効果の純粋な比較が可能である。

### 5.3 追加実験（言語最適化版の比較）

各シンタックスに固有の言語的慣用表現を活用した最適化版との比較実験。

| シンタックス | 使用ファイル |
|---|---|
| bridget | `bridget/context/example_11.md` |
| wenyan | `wenyan/context/example_11.md` |

この 2 ファイルは翻訳版ではなく、各シンタックスの表現を最大限に活用して独自に作成したコード例である。翻訳版との比較により、言語最適化が学習効果に与える影響を測定する。

### 5.4 example_33 の位置づけ

`example_33` は「HumanEval と重複しない問題を人手で作成した 33 件のコード例」として定義される。HumanEval ベンチマークとの独立性を担保するために人手で設計されており、翻訳版のみ（言語最適化版なし）で実験に使用する。

| シンタックス | 使用ファイル |
|---|---|
| yui | `yui/context/example_33.md` |
| bridget | `bridget/context/example_33_translated.md` |
| wenyan | `wenyan/context/example_33_translated.md` |

---

## 6. 翻訳方針

### 6.1 example_11_translated の翻訳方針

yui の `example_11.md` を各シンタックスへ直接翻訳する際の方針：

- **コードの構造・ロジック**：変更なし
- **コメント**：対象言語（英語 / 文言文）に翻訳
- **文字列リテラル**：対象言語に翻訳
- **関数名・変数名**：対象言語に翻訳（wenyan は漢字、bridget は英語）
- **1 文字変数・短縮識別子**（`n`, `i`, `a`, `b` など）：ASCII のまま保持

### 6.2 example_33_translated の翻訳方針

同上。さらに wenyan 版では以下の命名規則を適用：

- **記述的な名前**：漢語に変換（例: `result`→`結果`、`balance`→`餘額`、`stack`→`堆`）
- **アルゴリズム名**：漢語に変換（例: `bubble_sort`→`泡沫排序`、`find`→`尋找`）
- **ROT13 入出力・スタックマシン命令文字列**：ASCII のまま保持
- **オブジェクトキー**（`min`/`max`/`sum`/`count` など）：ASCII のまま保持

---

## 7. ファイルサイズ集計

| シンタックス | ファイル数 | 合計行数 |
|---|---|---|
| yui/context/ | 7 | 4,472行 |
| bridget/context/ | 8 | 4,758行 |
| wenyan/context/ | 8 | 5,158行 |
