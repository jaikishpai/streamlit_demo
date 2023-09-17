import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, time

st.header("Demo App")
st.info("st.write")
st.write("Hello, *World!* :sunglasses:")
st.write(1234)
df = pd.DataFrame({
    "first": [1, 2, 3],
    "second": [12, 13, 14]
})
st.write(df)

st.info("st.slider")
st.subheader("Range Slider")
values = st.slider("Select Range of values", 0.0, 100.0, (25.0, 75.0), )
st.write("Values:", values)

st.subheader("Range Time Slider")
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader("Datatime Slider")
start_time = st.slider("when do you start?", value=datetime(2020,1,1,9,30)), format("MM/DD/YY - hh:mm")
st.write("Start Time:", start_time)

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')