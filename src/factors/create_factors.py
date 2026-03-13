import numpy as np
import pandas as pd


def generate_return_features(df):
    # Sort DF First format of df index is [Ticker, Date]
    df.sort_index(ascending=True, inplace=True)
    # Create Simple Returns
    df["simple_returns"] = df["close"].groupby("ticker").pct_change()
    # Create Log Returns
    df["log_returns"] = np.log(df["close"]).groupby("ticker").diff()
    # Create BPS
    df["bps"] = df["simple_returns"] * 100
    return df
