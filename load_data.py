from datetime import datetime

import requests
from loguru import logger

from database.connection import client

date_from = "2015-01-01"

tickers = [
    'SBER', 'GAZP', 'LKOH', 'ROSN', 'NVTK', 'TATN', 'ALRS',
    'CHMF', 'MTSS', 'AFLT', 'POLY', 'KZOS', 'MTLR', 'YNDX',
    'DSKY', 'RUAL', 'SNGS', 'NLMK', 'MAGN', 'FIVE', 'SIBN',
    'IRAO', 'TRMK', 'BANE', 'MGTI', 'AERO', 'PRTK', 'CHMK',
    'KAZT', 'UPRO', 'PHOR', 'BSPB', 'KMAZ', 'MGNT', 'MRKC'
]

column_names = [
    'board_id', 'trade_date', 'short_name', 'sec_id',
    'num_trades', 'value', 'open_val', 'low_val', 'high_val',
    'legal_close_price', 'wap_price', 'close_val', 'volume',
    'market_price_2', 'market_price_3', 'admittedquote', 'mp_2_val_trd',
    'market_price_3_trades_value', 'admittedvalue', 'waval', 'trading_session',
    'curren_cyid', 'trendclspr'
]


def upload_data(items: list, ticker: str):
    for item in items:
        item[1] = datetime.strptime(item[1], '%Y-%m-%d').date()
        item[19] = item[19] if item[19] is not None else 0  # waval
    try:
        client.insert(
            'records',
            items,
            column_names=column_names
        )
    except Exception as e:
        logger.error(ticker)
        logger.error(e)


if __name__ == "__main__":

    for ticker in tickers:
        logger.success(f"Start ticker {ticker}. Date from {date_from}")
        url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/{ticker}.json?from={date_from}&start=0"
        try:
            response = requests.get(url=url)
        except Exception as e:
            logger.error(e)
            continue
        data = response.json()
        records = data["history"]["data"]
        upload_data(items=records, ticker=ticker)
        index, total, page_size = data["history.cursor"]["data"][0]
        total_page = total // page_size

        for i in range(1, total_page + 1):
            logger.info(f"{ticker} - Page {i}/{total_page}")
            url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/{ticker}.json?from={date_from}&start={i * 100}"
            try:
                response = requests.get(url=url)
            except Exception as e:
                logger.error(e)
                continue
            data = response.json()
            records = data["history"]["data"]
            upload_data(items=records, ticker=ticker)
