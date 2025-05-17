import numpy
import talib

close = numpy.random.random(100)

output = talib.SMA(close)

def main(name: str):
    print(f'hello, {name}!')

