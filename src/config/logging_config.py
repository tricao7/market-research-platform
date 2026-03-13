import logging
import sys

LOG_LEVEL = logging.DEBUG


def setup_logging():
    format = "%(asctime)s %(levelname)s %(filename)s: %(message)s"
    logging.basicConfig(
        format=format,
        filename="MRP.log",  # Use this if you want file
        # stream=sys.stdout, # Use this if you want in console
        encoding="utf-8",
        level=LOG_LEVEL,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
