import talib
import numpy as np

class SMA():
    def __init__(self, in_real: np.ndarray, period: int = 20):
        self.in_real = in_real
        self.period = period
        self.out_real = self.calculate()

    def calculate(self):
        out_real = talib.SMA(self.in_real, self.period)
        return out_real




