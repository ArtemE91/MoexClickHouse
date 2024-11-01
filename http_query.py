from time import sleep

import requests
from loguru import logger

from load_data import tickers


def start():
    while True:
        for ticker in tickers:
            logger.success(f"Start {ticker}")
            url = f"http://127.0.0.1:5000/moex/{ticker}"
            requests.get(url)
            sleep(1)


if __name__ == "__main__":
    start()
