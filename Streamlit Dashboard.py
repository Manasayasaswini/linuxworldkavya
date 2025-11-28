import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Title and intro
st.title("Streamlit App of VGU")
st.text("Welcome to our dashboard")
st.header("I am a header")
st.write("You can write:", 10 + 5)

# User inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
course = st.selectbox("Enter your course:", ["BCA", "BTECH", "MCA"])

st.write("Your name is:", name)
st.write("Your age is:", age)
st.write("Your course is:", course)

# Button
if st.button("Click me"):
    st.success("Button clicked!")

# File upload
file = st.file_uploader("Upload your CSV file", type=["csv"])
if file is not None:
    df_uploaded = pd.read_csv(file)
    st.write("File uploaded successfully!")
    st.dataframe(df_uploaded)

# Example DataFrame
data = {"Name": ["Tom", "Jack", "Ravi"], "Marks": [10, 20, 10]}
df = pd.DataFrame(data)
st.subheader("Sample DataFrame")
st.dataframe(df)

# Charts
st.subheader("Charts")
chart_data = pd.DataFrame({"Marks": [10, 20, 10]}, index=["Tom", "Jack", "Ravi"])
st.line_chart(chart_data)
st.bar_chart(chart_data)

# Pie chart
st.subheader("Pie Chart")
subjects = ["Python", "C++", "Java"]
marks = [10, 20, 10]

fig, ax = plt.subplots()
ax.pie(marks, labels=subjects, autopct="%1.1f%%")
st.pyplot(fig)
