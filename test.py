import numpy as np
from CryptoData import CryptoData
from FastExpression import *
from QuantAnalysis import QuantAnalysis
import pandas as pd

BTC = CryptoData("BTC")
print(BTC.df)
print(BTC.getElement("close"))

print(vwap(BTC))

data = {
    "BTC": {
        "algorithm1" : QuantAnalysis(BTC).algorithm1(),
        "algorithm2": QuantAnalysis(BTC).algorithm2(),
        "algorithm3": QuantAnalysis(BTC).algorithm3(),
        "algorithm4": QuantAnalysis(BTC).algorithm4(),
        "algorithm5": QuantAnalysis(BTC).algorithm5(),
    }
}
print(data)
df = pd.DataFrame.from_dict(data,orient="index")
print(df)
