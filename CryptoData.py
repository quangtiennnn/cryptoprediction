import sys
import requests
from datetime import datetime
import pandas as pd
import os
"""PATH"""

API_KEY = "92TJMSJYSE7VYVKU"
API_ENDPOINT = "https://www.alphavantage.co/query"

class CryptoData:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.df = self.getData()
        #Define OLHC:
        self.open = self.df["open"]
        self.high = self.df["high"]
        self.low = self.df["low"]
        self.close = self.df["close"]
        self.volume = self.df["volume"]
        self.cap = self.df["cap"]

    def getData(self):
        parameters = {
            "function": "DIGITAL_CURRENCY_DAILY",
            "symbol": self.symbol,
            "market": "USD",
            "apikey": API_KEY,
        }
        try:
            response = requests.get(url=API_ENDPOINT, params=parameters)
            data = response.json()['Time Series (Digital Currency Daily)']
        except KeyError:
            print('Visit "https://www.alphavantage.co/digital_currency_list" for more information about symbol name.')
            sys.exit()
        except:
            print("Something when wrong. Try again")
            sys.exit()
        df = pd.DataFrame.from_dict(data, orient= "index")
        df.index = pd.to_datetime(df.index)
        df.index.name = 'date'
        #data proccesing
        df = df.drop(["1b. open (USD)","2b. high (USD)","3b. low (USD)","4b. close (USD)"], axis = 1).sort_index()
        df.rename(columns={
            '1a. open (USD)': 'open',
            '2a. high (USD)': 'high',
            '3a. low (USD)' : 'low',
            '4a. close (USD)': 'close',
            '5. volume' : 'volume',
            '6. market cap (USD)': 'cap',
            }, inplace=True)
        df = df.astype(
            {
                'open': 'float',
                'high': 'float',
                'low': 'float',
                'close': 'float',
                'volume': 'float',
                'cap': 'float',
            }
        )
        return df