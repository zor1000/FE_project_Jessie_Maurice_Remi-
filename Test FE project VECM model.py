
# pip install yfinance
import os
os.environ['APPDATA'] = ''
import pandas as pd
import yfinance as yf
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from pandasgui import show


tickers = ['META','AMZN','AAPL','NFLX','GOOG']
# Grab datas
df = yf.download(tickers)
df = df['Adj Close'].dropna()
data = pd.DataFrame(df)

#gui = show(data)

df.tail()
data_2 = pd.DataFrame(df.tail())
gui = show(data_2)

df.plot(subplots=True);


