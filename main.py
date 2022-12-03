from CryptoData import CryptoData
import numpy as np
import matplotlib as mpl
# import matplotlib.pyplot as plt
import pandas as pd
import datetime

BTC = CryptoData("BTC")
df1 = BTC.df
df1.to_csv("out.csv")

# y = BTC.getTimeSeries()
# x = np.array(BTC.getElement("close"))


