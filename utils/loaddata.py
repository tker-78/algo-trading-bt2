import pandas as pd


def load_csv(filepath: str):

    headers = ["datetime", "open", "high", "low", "close", "volume"]

    with open(filepath, "r") as f:
        # ファイルの列数がheadersの項目数と一致しない場合、例外を投げる
        first_line = f.readline().strip()
        if first_line and len(first_line.split("\t")) != len(headers):
            raise ValueError("The number of columns in the file does not match the expected headers.")
        



    df = pd.read_csv(filepath,
                     header=None,
                     names=headers,
                     sep="\t",
                     encoding="utf-8")
    return df



