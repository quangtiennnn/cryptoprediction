from FastExpression import *
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import math
import pandas as pd

class SmaCross(Strategy):
    n1 = 10
    n2 = 20
    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

class RSI(Strategy):
    def init(self):
        close = self.data.Close
        self.rsi = rsi(self.data)
    def next(self):
        if self.rsi < 30:
            self.position.close()
            self.buy()
        if self.rsi > 70:
            self.position.close()
            self.buy()


    # def marketTrend(self):
    #     for level in range(1,4):
    #         if adx(self.df) < 25*level:
    #             return level

    # #20-10-2022
    # def algorithm1(self):
    #     close_mean20 = ts_mean(self.close, 20)
    #     return round(100* -(self.close[-1] - close_mean20)/close_mean20,5)
    #
    # def algorithm2(self):
    #     return round(100* -ts_max_diff(self.close,5)/ts_max(self.close,5),5)
    #
    # def algorithm3(self):
    #     # volume_mean360 = ts_mean(self.volume,360)
    #     # close_mean20 = ts_mean(self.close,20)
    #     # print(100*(self.volume[-1] - volume_mean360) / volume_mean360)
    #     # print(self.close[-1]-close_mean20)
    #     # return round(100* -signed_power(self.close[-1]-close_mean20, (self.volume[-1]-volume_mean360)/volume_mean360)/close_mean20,2)
    #     return 0
    #
    # def algorithm4(self):
    #     vwap20 = vwap(self.df,20)
    #     return round(math.log(vwap20[-1]/self.close[-1]),5)
    #
    # def algorithm5(self):
    #     return round(100*-(self.close[-1] - (ts_max(self.close, 20) + ts_min(self.close, 20))/2) / self.low[-1],5)



