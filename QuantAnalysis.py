from FastExpression import *
from CryptoData import CryptoData
import math

class QuantAnalysis:
    def __init__(self, data: CryptoData):
        self.df = data
        self.open = self.df.getElement("open")
        self.high = self.df.getElement("high")
        self.low = self.df.getElement("low")
        self.close = self.df.getElement("close")
        self.volume = self.df.getElement("volume")
        self.cap = self.df.getElement("cap")
        self.len = len(self.close)

    #20-10-2022
    def algorithm1(self):
        close_mean20 = ts_mean(self.close, 20)
        return round(100* -(self.close[-1] - close_mean20)/close_mean20,5)

    def algorithm2(self):
        return round(100* -ts_max_diff(self.close,5)/ts_max(self.close,5),5)

    def algorithm3(self):
        # volume_mean360 = ts_mean(self.volume,360)
        # close_mean20 = ts_mean(self.close,20)
        # print(100*(self.volume[-1] - volume_mean360) / volume_mean360)
        # print(self.close[-1]-close_mean20)
        # return round(100* -signed_power(self.close[-1]-close_mean20, (self.volume[-1]-volume_mean360)/volume_mean360)/close_mean20,2)
        return 0

    def algorithm4(self):
        vwap20 = vwap(self.df,20)
        return round(math.log(vwap20[-1]/self.close[-1]),5)

    def algorithm5(self):
        return round(100*-(self.close[-1] - (ts_max(self.close, 20) + ts_min(self.close, 20))/2) / self.low[-1],5)

