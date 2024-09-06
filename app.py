import pandas as pd
import streamlit as st

st.write("Hello world")

st.title("Hello :blue[world]")
st.title("Hello :red[world]")
st.title("Hello :green[world] :sunglasses:")

st.write(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}))

st.link_button("Click here", "https://www.streamlit.io")

st.header("This is a header", divider="rainbow")
st.header("This is a header", divider="blue")
st.header("This is a header", divider="green")
st.header("This is a header", divider="orange")
st.header("This is a header", divider="red")
st.header("This is a header", divider="violet")
st.header("This is a header", divider="gray")

code = """print("Hello world")"""
st.code(code, language="python")

agree = st.checkbox("Check me out")
if agree:
    st.write("Great!")

options = st.multiselect("Pick a color", ["red", "green", "blue"])

st.write("You selected:", options)


options = st.radio("Pick a color", ["red", "green", "blue"])

st.write("You selected:", options)

df = pd.DataFrame({"色番号": [1, 2, 3], "レート": [4, 5, 6], "mark": [True, True, True]})
edited_df = st.data_editor(df)
st.write(edited_df.loc[edited_df["レート"].idxmax()]["色番号"])
