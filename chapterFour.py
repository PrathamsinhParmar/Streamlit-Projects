import streamlit as st
import pandas as pd

st.title("Employee Salary Predictor")
file = st.file_uploader("Upload Your Dataset : ", ["csv" , "xlsx", "pdf"])

if file:
    data = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(data)

if file:
    st.subheader("Data Summary")
    st.write(data.describe())

if file:
    uniqueCountry = data["native-country"].unique()
    selectedCountry = st.selectbox("Select A Country : ", uniqueCountry)
    filteredCountry = data[data["native-country"] == selectedCountry]
    st.dataframe(filteredCountry)
