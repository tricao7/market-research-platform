import json
import logging
import os

import requests
from jsonschema import validate

logger = logging.getLogger(__name__)
# Load the environment variables
TIINGO_API_KEY = os.getenv("TIINGO_API_KEY")

tiingo_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "date": {"type": "string", "format": "date-time"},
            "close": {"type": "number"},
            "high": {"type": "number"},
            "low": {"type": "number"},
            "open": {"type": "number"},
            "volume": {"type": "number"},
            "adjClose": {"type": "number"},
            "adjHigh": {"type": "number"},
            "adjLow": {"type": "number"},
            "adjOpen": {"type": "number"},
            "adjVolume": {"type": "number"},
            "divCash": {"type": "number"},
            "splitFactor": {"type": "number"},
        },
    },
}


def ticker_session_request(tickers, start_date, end_date):
    base_url = "https://api.tiingo.com/tiingo/daily/"
    request_dct = {}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {TIINGO_API_KEY}",
    }
    params = {"startDate": start_date, "endDate": end_date}
    with requests.Session() as s:
        s.headers.update(headers)
        for ticker in tickers:
            request_info = {}
            try:
                url = base_url + f"{ticker}/prices"
                r = s.get(url=url, params=params, timeout=100)
                # Will raise an error if the status is not successful
                r.raise_for_status()
                # validate Json
                data = r.json()
                # Will raise an error if the schema does not match
                validate(instance=data, schema=tiingo_schema)
                ## Create request info ##
                request_info["ticker"] = ticker
                request_info["url"] = url
                request_info["status"] = r.status_code
                request_info.update(params)
                #########################
                logger.info(f"Request Info: {request_info}")
                request_dct[ticker] = {
                    "metadata": "<INSERT METADATA>",
                    "request_info": request_info,
                    "data": data,
                }
            except Exception as e:
                print(f"Error: {e}")
    return request_dct
