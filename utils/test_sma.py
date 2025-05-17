from indicator import SMA
import numpy as np

import pytest

# Test function to validate SMA real-world data
def test_valid_data():
    test_in_real = np.array([1, 2, 3, 4, 5, 6], dtype=float)  # Example data
    test_period = 3
    sma = SMA(test_in_real, test_period)  # Initialize SMA with a period of 3
    sma.calculate()  # Perform SMA calculation
    expected = np.array([np.nan, np.nan, 2.0, 3.0, 4.0, 5.0])

    assert sma.out_real == pytest.approx(expected, nan_ok=True)

def test_invalid_data():
    test_in_real = [1,2,3,4,5,6]
    test_period = 3
    with pytest.raises(TypeError):
        sma = SMA(test_in_real, test_period)

def test_empty_data():
    test_in_real = np.array([])
    test_period = 3
    sma = SMA(test_in_real, test_period)
    sma.calculate()
    expected = np.array([])

    assert sma.out_real == pytest.approx(expected)




