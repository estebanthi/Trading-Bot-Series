from enum import Enum
import backtrader as bt


class Timeframes(Enum):
    m1 = (bt.TimeFrame.Minutes, 1)
    m5 = (bt.TimeFrame.Minutes, 5)
    m15 = (bt.TimeFrame.Minutes, 15)
    m30 = (bt.TimeFrame.Minutes, 30)
    h1 = (bt.TimeFrame.Minutes, 60)
    h4 = (bt.TimeFrame.Minutes, 240)
    d1 = (bt.TimeFrame.Days, 1)
    w1 = (bt.TimeFrame.Weeks, 1)
    mo1 = (bt.TimeFrame.Months, 1)
