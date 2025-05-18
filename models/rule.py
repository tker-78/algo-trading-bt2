from typing import List


from utils.indicator import Indicator
from .signal import Signal


class Rule():
    def __init__(self):
        self.indicators = list()

    def add_indicator(self, indicator: Indicator):
        self.indicators.append(indicator)

class SMAGolden(Rule):

    def __init__(self, periods: List[int]):
        super().__init__()
        self.periods = periods

    def make_signal(self) -> List[Signal]:
        ...

