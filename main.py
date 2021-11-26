import streamlit as st
import pandas

data = {
  'Series_1': [1, 3, 4, 5, 7],
  'Series_2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)


st.title("1app")
st.subheader("intro")
st.write("webapp")
st.write(df)