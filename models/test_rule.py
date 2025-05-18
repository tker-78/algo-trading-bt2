from .rule import SMAGolden
from datetime import datetime

def test_indicator():
    """
    インジケータの種類が正しいこと
    """
    rule_smag = SMAGolden("data/test_data.csv", 3, 10)
    assert rule_smag.indicator == "sma"

def test_data():
    """
    csvの全データが読み込まれていること
    """
    filepath = "data/test_data.csv"
    count = 0
    with open(filepath, "r") as f:
        count = len(f.readlines() )


    rule_smag = SMAGolden(filepath, 3, 10)
    assert rule_smag.data is not None
    assert len(rule_smag.data) == count


def test_make_signal():
    filepath = "data/test_data.csv"
    rule_smag = SMAGolden(filepath, 10, 50)
    signal_list = rule_smag.make_signal()

    for signal in signal_list:
        print(signal.time, signal.price, signal.side)

    assert signal_list is not None
    assert len(signal_list) > 0

    for signal in signal_list:
        assert isinstance(signal.time, datetime)
        assert isinstance(signal.side, str)
        assert isinstance(signal.price, float)

