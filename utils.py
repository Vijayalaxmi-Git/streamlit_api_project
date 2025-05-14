# Utility functions for the Streamlit application

import requests
import pandas as pd 
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
class StockAPI:

    def __init__(self):
        self.api_key = st.secrets["API_KEY"]
        self.url = "https://alpha-vantage.p.rapidapi.com/query"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
        }

    def symbol_search(self, company: str) -> pd.DataFrame:
        querystring = {
            "datatype": "json",
            "keywords": company,
            "function": "SYMBOL_SEARCH",
        }
        response = requests.get(url=self.url, headers=self.headers, params=querystring)
        data = response.json()["bestMatches"]
        return pd.DataFrame(data)

    def stock_data(self, symbol: str) -> pd.DataFrame:
        querystring = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "compact",
            "datatype": "json",
        }
        response = requests.get(url=self.url, headers=self.headers, params=querystring)
        data2 = response.json()["Time Series (Daily)"]
        res2 = pd.DataFrame(data2).T

        # Convert output to float
        res2 = res2.astype(float)

        # Conert to index to datetime
        res2.index = pd.to_datetime(res2.index)

        return res2

    def plot_chart(self, df: pd.DataFrame) -> go.Figure:
        fig = go.Figure(
            data=[
                go.Candlestick(
                        x=df.index,
                        open=df["1. open"],
                        high=df["2. high"],
                        low=df["3. low"],
                        close=df["4. close"],
                        increasing=dict(line=dict(color='green'), fillcolor='green'),
                        decreasing=dict(line=dict(color='red'), fillcolor='red'),
                )
            ]
        )

        fig.update_layout({"width": 1000, "height": 800})
        return fig
