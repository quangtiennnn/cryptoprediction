import numpy as np
from CryptoData import CryptoData
from FastExpression import *
from QuantAnalysis import QuantAnalysis
import pandas as pd
# import talib as ta
import pandas_ta as ta

BTC = CryptoData("BTC")
print(BTC.df)
close = BTC.getElement("close")

print(SMA(BTC))
#
# data = {
#     "BTC": {
#         "algorithm1" : QuantAnalysis(BTC).algorithm1(),
#         "algorithm2": QuantAnalysis(BTC).algorithm2(),
#         "algorithm3": QuantAnalysis(BTC).algorithm3(),
#         "algorithm4": QuantAnalysis(BTC).algorithm4(),
#         "algorithm5": QuantAnalysis(BTC).algorithm5(),
#     }
# }
# print(data)
# df = pd.DataFrame.from_dict(data,orient="index")
# print(df)
# close = np.random.random(100)
arr = np.array(close)
output = ta.SMA(arr,20)
print(output)
upper, middle, lower = ta.BBANDS(arr, matype=ta.MA_Type.T3,timeperiod =20)
print(upper[-1])
print(middle[-1])
print(lower[-1])

