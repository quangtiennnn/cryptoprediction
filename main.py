from CryptoData import CryptoData
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

BTC = CryptoData("BTC")
y = BTC.getTimeSeries()
x = np.array(BTC.getElement("close"))


