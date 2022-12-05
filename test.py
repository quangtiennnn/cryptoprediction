import numpy as np
from CryptoData import CryptoData
from FastExpression import *
# from QuantAnalysis import QuantAnalysis
import matplotlib.pyplot as plt
# import talib as ta
import pandas_ta as ta
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
BTC = CryptoData("BTC")
df = BTC.df

df1 = df.ta.cdl_pattern(name="all")
df1.to_csv("out.csv")

# calculate MACD values
# df.ta.macd(close='close', fast=12, slow=26, append=True)

# Force lowercase (optional)
# df.columns = [x.lower() for x in df.columns]