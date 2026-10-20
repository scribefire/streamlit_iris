# Streamlit UI と Iris分類デモ

Streamlitのマルチページ構成で、ダッシュボード部品と基本的な分類モデルを試す小さなアプリです。

## ページ構成

- **メインページ（`app.py`）**：テキスト、ボタン、選択ウィジェット、データエディター、Pandasの表を表示します。
- **可視化（`pages/page1.py`）**：ランダム生成したサンプルデータを棒グラフ、折れ線グラフ、散布図、地図で表示します。
- **Iris分類（`pages/page2.py`）**：scikit-learn付属のIrisデータセットで決定木を学習し、評価スコアと、入力値に対する品種予測・予測確率を表示します。

Streamlitが`pages/`以下を自動的にページとして読み込みます。

## ローカルでの起動

Python 3とpipを使います。リポジトリのルートで実行してください。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install streamlit pandas numpy matplotlib scikit-learn
streamlit run app.py
```

Streamlitが表示するURL（通常は http://localhost:8501 ）をブラウザーで開きます。

## 実装メモ

- 可視化ページの値は実データではなく、実行時にランダム生成しています。
- Irisページはscikit-learn付属のデータを使うため、別途データをダウンロードする必要はありません。
- ページの再実行時にモデルを学習します。データ分割を固定していないため、評価スコアは実行ごとに変わることがあります。

## ファイル構成

```text
app.py
pages/
  page1.py
  page2.py
```

Streamlitとscikit-learnの基本機能を試す学習用デモであり、本番用の予測サービスではありません。
