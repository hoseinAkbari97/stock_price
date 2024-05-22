import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App

shown are stock closing price and volume of Google!

""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2013-6-28', end='2023-6-11')
# Open  High    Low Close   Volume  Dividends   Stock   Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)