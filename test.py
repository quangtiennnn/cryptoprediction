import numpy as np
from CryptoData import CryptoData
# from FastExpression import *
from QuantAnalysis import QuantAnalysis
import pandas as pd
# import talib as ta
import pandas_ta as ta

BTC = CryptoData("BTC")
df = BTC.df
print(df)
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
df.ta.indicators()
# df1 = df.ta.vwap().values.tolist()
# print(df1)

# ta.help
help(ta.cdl_pattern)
df1 = df.ta.cdl_pattern()
print(df1)
df1.to_csv("out.csv")