# StreamlitとIris分類のデモ

Streamlitの画面部品とグラフを試しながら、scikit-learnのIrisデータで品種分類を行う小さなマルチページアプリです。

## ページ

- `app.py`：ボタン、選択ウィジェット、データエディターなど
- `pages/page1.py`：ランダム生成した値を棒・折れ線・散布図と地図で表示
- `pages/page2.py`：決定木を学習し、入力した花の計測値から品種と予測確率を表示

## 起動

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install streamlit pandas numpy matplotlib scikit-learn
streamlit run app.py
```

Irisデータはscikit-learnに含まれているため、別途ダウンロードは不要です。分類ページは表示のたびに学習・評価するので、スコアは実行ごとに変わります。
