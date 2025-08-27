import streamlit as st
import pandas as pd
import requests

st.markdown('''# **Binance Price App**
 A Simple Crypto Currency Price App, Pulling Price Data From **Binance**
            ''')

st.header("Selected Prices")

url = "https://api.binance.com/api/v3/ticker/24hr"
responce = requests.get(url)

if responce.status_code == 200:
    data = pd.read_json(url)
else:
    st.error(f"Failed to fetch data. Status code: {responce.status_code}")


def round_value(input_value):
    if(input_value.values > 1):
        val = float(round(input_value, 2))
    else:
        val = float(round(input_value, 6))
    return val

col1 , col2 , col3 = st.columns(3)

st.sidebar.header("Select Your Coins")
col1_select = st.sidebar.selectbox("Price 1", data.symbol, list(data.symbol).index('ETHBTC'))
col2_select = st.sidebar.selectbox("Price 2", data.symbol, list(data.symbol).index('BNBBTC'))
col3_select = st.sidebar.selectbox("Price 3", data.symbol, list(data.symbol).index('BTCUSDT'))
col4_select = st.sidebar.selectbox("Price 4", data.symbol, list(data.symbol).index('GASBTC'))
col5_select = st.sidebar.selectbox("Price 5", data.symbol, list(data.symbol).index('XRPBUSD'))
col6_select = st.sidebar.selectbox("Price 6", data.symbol, list(data.symbol).index('DOGEBUSD'))
col7_select = st.sidebar.selectbox("Price 7", data.symbol, list(data.symbol).index('SHIBBUSD'))
col8_select = st.sidebar.selectbox("Price 8", data.symbol, list(data.symbol).index('DOTBUSD'))
col9_select = st.sidebar.selectbox("Price 9", data.symbol, list(data.symbol).index('ADABUSD'))


col1_data = data[data.symbol == col1_select]
col2_data = data[data.symbol == col2_select]
col3_data = data[data.symbol == col3_select]
col4_data = data[data.symbol == col4_select]
col5_data = data[data.symbol == col5_select]
col6_data = data[data.symbol == col6_select]
col7_data = data[data.symbol == col7_select]
col8_data = data[data.symbol == col8_select]
col9_data = data[data.symbol == col9_select]


col1_price = round_value(col1_data.weightedAvgPrice)
col2_price = round_value(col2_data.weightedAvgPrice)
col3_price = round_value(col3_data.weightedAvgPrice)
col4_price = round_value(col4_data.weightedAvgPrice)
col5_price = round_value(col5_data.weightedAvgPrice)
col6_price = round_value(col6_data.weightedAvgPrice)
col7_price = round_value(col7_data.weightedAvgPrice)
col8_price = round_value(col8_data.weightedAvgPrice)
col9_price = round_value(col9_data.weightedAvgPrice)


col1_persentage = f"{float(col1_data.priceChangePercent)}%"
col2_persentage = f"{float(col2_data.priceChangePercent)}%"
col3_persentage = f"{float(col3_data.priceChangePercent)}%"
col4_persentage = f"{float(col4_data.priceChangePercent)}%"
col5_persentage = f"{float(col5_data.priceChangePercent)}%"
col6_persentage = f"{float(col6_data.priceChangePercent)}%"
col7_persentage = f"{float(col7_data.priceChangePercent)}%"
col8_persentage = f"{float(col8_data.priceChangePercent)}%"
col9_persentage = f"{float(col9_data.priceChangePercent)}%"

col1.metric(col1_select , col1_price , col1_persentage)
col2.metric(col2_select , col2_price , col2_persentage)
col3.metric(col3_select , col3_price , col3_persentage)
col1.metric(col4_select , col4_price , col4_persentage)
col2.metric(col5_select , col5_price , col5_persentage)
col3.metric(col6_select , col6_price , col6_persentage)
col1.metric(col7_select , col7_price , col7_persentage)
col2.metric(col8_select , col8_price , col8_persentage)
col3.metric(col9_select , col9_price , col9_persentage)

st.subheader("All Coin Prices")
st.dataframe(data)

st.info("Credit : Created By Prathamsinh Parmar")
