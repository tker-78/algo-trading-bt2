from datetime import datetime

class Signal():
    def __init__(self, side: str, time: datetime ):
        self.side = side
        self.time = time
