import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.slider("Amount To Convert", 1,1000000,200000)

targeted_currency = st.selectbox("Select Currency", ["USD", "EUR", "GBP", "INR", "AED" , "AFN", "ALL" , "AMD" , "ANG" , "AUD" , "BDT" , "BOB" , "BRL"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()
        rate = data["rates"][targeted_currency]
        converted_amount = rate * amount    
        st.success(f"{amount} INR = {converted_amount:.2f} {targeted_currency}")
    else:
        st.error("Error fetching exchange rates. Please try again later.")