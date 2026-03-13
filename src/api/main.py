import logging
import os

from dotenv import load_dotenv

from src.config.logging_config import setup_logging

# Load environment variables
load_dotenv()

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


def main():
    pass


if __name__ == "__main__":
    logging.info("Welocome to MRP")
