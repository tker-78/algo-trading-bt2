from typing import List
from utils.loaddata import load_csv
import pandas as pd
from datetime import datetime


from utils.indicator import Indicator, SMA
from .signal import Signal


class Rule():
    def __init__(self, filepath: str):
        self.data = load_csv(filepath)


class SMAGolden(Rule):

    def __init__(self,
                 filepath: str,
                 period1: int,
                 period2: int):
        super().__init__(filepath)
        self.indicator = "sma"
        self.sma1 = None
        self.sma2 = None

        # 常にperiod1 <= period2とする
        if period1 > period2:
            period1, period2 = period2, period1

        self.sma1 = SMA(self.data.close, period1).out_real
        self.sma2 = SMA(self.data.close, period2).out_real

    def make_signal(self) -> List[Signal]:
        signal_list = list()
        for i in range(len(self.data)-1):
            if self.sma1[i] <=  self.sma2[i] and self.sma1[i+1] > self.sma2[i+1]:
                time = datetime.strptime(self.data.loc[i+1].datetime, "%Y-%m-%d %H:%M" )
                price = self.data.loc[i+1].close
                signal = Signal(time, price, "buy")
                signal_list.append(signal)
            elif self.sma1[i] >= self.sma2[i] and self.sma1[i+1] < self.sma2[i+1]:
                time = datetime.strptime(self.data.loc[i+1].datetime, "%Y-%m-%d %H:%M" )
                price = self.data.loc[i+1].close
                signal = Signal(time, price, "sell")
                signal_list.append(signal)
        return signal_list





