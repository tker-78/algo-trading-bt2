from datetime import datetime

class Signal():
    def __init__(self,  time: datetime, price: float, side: str ):
        self.time = time
        self.price = price
        self.side = side
