import pytest
import os
from pathlib import Path
from .loaddata import load_csv

def test_valid_csv(tmp_path):

    filename = "test.csv"
    test_csv_content = "2001-01-01 00:00:00\t100\t105\t95\t102\t2000\n"
    test_csv_content += "2001-01-01 01:00:00\t100\t105\t95\t102\t2000\n"

    test_file = os.path.join(tmp_path, filename)
    with open(test_file, "w") as f:
        f.write(test_csv_content)

    df = load_csv(test_file)

    assert df is not None
    assert df.columns.to_list() == ["datetime", "open", "high", "low", "close", "volume"]
    assert len(df) == 2
    assert df.open.iloc[0] == 100

def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        load_csv("non_esistent_file.csv")

def test_invalid_csv(tmp_path):
    filename = "invalid_format.csv"
    test_csv_content = "invalid\tdata\tformat\n100\t200\t300\n"

    test_file = os.path.join(tmp_path, filename)

    with open(test_file, "w") as f:
        f.write(test_csv_content)

    with pytest.raises(ValueError):
        df = load_csv(test_file)

def test_empty_csv(tmp_path):
    empty_file = Path(tmp_path) / "empty.csv"
    empty_file.touch()

    df = load_csv(empty_file)

    assert len(df) == 0

def test_csv_without_tab_separator(tmp_path):
    filename = "csv_without_tab_separator.csv"
    test_csv_content = "2020-01-01 00:00:00,100,200,300,400,500"

    test_file = os.path.join(tmp_path, filename)

    with open(test_file, "w") as f:
        f.write(test_csv_content)

    with pytest.raises(ValueError):
        load_csv(test_file)



