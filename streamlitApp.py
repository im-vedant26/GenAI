import streamlit as st
import pandas as pd
import numpy as np

st.title("My First App")
st.write(":streamlit: This is my first app using Streamlit!")
st.text(" Lets get started ")

name = st.text_input("Enter your name: ")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# df = pd.DataFrame(np.random.randn(10, 9), columns=['A','B'])
# st.line_chart(df)
# st.bar_chart(df)

upload_file = st.file_uploader("Upload CSV file", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is header")
st.subheader("This is subheader")
st.markdown(" **Bold**, *Italic*,'code, [link](https://streamlit.io/),  ")

st.text_input("What is your name")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0,max_value=100)
st.slider("choose a range",0,100)
st.selectbox("Pick a color",["Red","Green","Blue"])
st.multiselect("Pick multiple colors",["Red","Green","Blue"])


option = st.radio("choose view", ["show chart", "show table"])
if option == "show chart":
    st.write("Chart should appear")
else:
    st.write("Table should appear")


with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write(f"Hello {name}, you are {age} years old!")