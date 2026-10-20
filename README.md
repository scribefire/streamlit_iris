# Streamlit UI and Iris Classification Demo

A small multi-page Streamlit application for exploring common dashboard components and a basic machine-learning classification workflow.

## Pages

- **Main page — `app.py`**: examples of Streamlit text, buttons, selection widgets, a data editor, and a small Pandas table.
- **Visualizations — `pages/page1.py`**: generated sample data displayed as bar, line, scatter, and map charts.
- **Iris classifier — `pages/page2.py`**: trains a decision-tree classifier with scikit-learn's built-in Iris dataset, shows an evaluation score, and predicts a species from user-entered measurements.

Streamlit discovers the pages under `pages/` automatically.

## Run locally

Python 3 and pip are required. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install streamlit pandas numpy matplotlib scikit-learn
streamlit run app.py
```

Open the local URL printed by Streamlit, usually http://localhost:8501.

## Implementation notes

- The first visualization page uses randomly generated sample data; it is not a real student dataset.
- The Iris page uses the dataset bundled with scikit-learn, so no separate data download is needed.
- The model is trained when the page runs. The train/test split is random, so the displayed evaluation score can vary between runs.

## Repository layout

```text
app.py
pages/
  page1.py
  page2.py
```

This repository is a compact Streamlit and scikit-learn learning demo, not a production prediction service.
