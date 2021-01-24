import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price Web App

Shown are the stock **closing** price of Tesla for the past decade

""")

tickerSymbol = "TSLA"
tickerData = yf.Ticker(tickerSymbol)
tickerOf = tickerData.history(period="1d", start="2010-12-31", end="2021-1-1")

st.line_chart(tickerOf.Close)
# st.line_chart(tickerOf.Volume)

st.write("""

Shown are the stock **closing** price of Amazon for the past decade

""")

tickerSymbol = "AMZN"
tickerData = yf.Ticker(tickerSymbol)
tickerOf = tickerData.history(period="1d", start="2010-12-31", end="2021-1-1")

st.line_chart(tickerOf.Close)