import streamlit as st
import numpy as np
import pandas as pd

st.header("st.write")
st.write("Hello, *World!* :sunglasses:")
st.write(1234)
df = pd.DataFrame({
    "first": [1, 2, 3],
    "second": [12, 13, 14]
})
st.write(df)
