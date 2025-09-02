from pandas_datareader import data
import pandas as pd
import os
import datetime as dt
import urllib.request, json
import numpy as np
import tensorflow as tf 
from sklearn.preprocessing import MinMaxScaler
import requests
import matplotlib.pyplot as plt


api_key = '477YEHL3M5S0HVNY'
ticker = 'AAPL'
url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

file_to_save = r'stock_market_data-%s.csv'%ticker
if not os.path.exists(file_to_save):
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            # extract stock market data
            data = data['Time Series (Daily)']
            df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d')
                data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                            float(v['4. close']),float(v['1. open'])]
                df.loc[-1,:] = data_row
                df.index = df.index + 1
        print('Data saved to : %s'%file_to_save)        
        df.to_csv(file_to_save)

    # If the data is already there, just load it from the CSV
else:
    print('File already exists. Loading data from CSV')
    df = pd.read_csv(file_to_save)

df = df.sort_values("Date")
df.head

plt.figure(figsize = (18,9))
plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
plt.show()

high_prices = df.loc[:,"High"].to_numpy()
low_prices = df.loc[:, "Low"].to_numpy()
mid_price = (high_prices + low_prices)/2.0

train_data = mid_price[:11000]
test_data = mid_price[11000:]
