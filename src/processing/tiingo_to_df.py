import logging

import pandas as pd

logger = logging.getLogger(__name__)


def convert_tiingo_payload(tiingo_dct, format="long"):
    df = pd.DataFrame()
    for ticker, payload in tiingo_dct.items():
        ticker_df = pd.DataFrame(payload.get("data"))
        ticker_df["ticker"] = ticker
        # Convert date to date:
        ticker_df["date"] = pd.to_datetime(ticker_df["date"])
        df = pd.concat([df, ticker_df])
    df.set_index(["ticker", "date"], inplace=True)
    return df
