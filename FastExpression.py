from CryptoData import CryptoData
from statistics import *
# import talib as ta
import pandas_ta as ta

"""OPERATOR"""



def accumulationList(num_list: list, lookback_days=20):
    return [sum(num_list[y - lookback_days:y]) for y in range(lookback_days, len(num_list) + 1)]


def ifTrue(condition: bool) -> int:
    if (condition == True):
        return 1
    else:
        return 0

def sign(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1


def signed_power(x, y):
    return sign(x) * (pow(abs(x),y))

# def sign(list: list):
#     number = list[-1]
#     if number > 0:
#         return 1
#     elif number == 0:
#         return 0
#     else:
#         return -1
#
#
# def signed_power(list_x: list, list_y: list):
#     return sign(list_x[-1]) * (pow(abs(list_x[-1]), list_y[-1]))


"""TIME SERIES"""
def ts_sum(list: list, lookback_days: int):
    return accumulationList(list,lookback_days)

def ts_mean(list: list, lookback_days: int):
    return sum(list[-lookback_days:]) / lookback_days


def ts_max(list: list, lookback_days: int):
    return max(list[-lookback_days:])


def ts_min(list: list, lookback_days: int):
    return min(list[-lookback_days:])


def ts_max_diff(list: list, lookback_days: int):
    return  list[-1] - ts_max(list, lookback_days)


def ts_min_diff(list: list, lookback_days: int):
    return list[-1] - ts_min(list, lookback_days)


def ts_delay(list: list, lookback_days: int):
    return list[-lookback_days]


def ts_delta(list: list, lookback_days: int):
    return list[-1] - ts_delay(list, lookback_days)


def ts_std_dev(list: list, lookback_days: int):
    return [0] * (lookback_days - 1) + [stdev(list[y - lookback_days:y]) for y in range(lookback_days, len(list) + 1)]


"""INDICATOR"""
#VWAP
def vwap(DataFrame):
    return DataFrame.ta.vwap().values.tolist()

def adx(DataFrame):
    return DataFrame.ta.adx()["ADX_14"].tolist()










