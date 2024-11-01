import pytest

from database.query import get_data_by_ticker, insert_data_mongo, get_aggr_volume_by_ticker


@pytest.mark.parametrize("ticker", ("SBER", ))
def test_get_data_by_ticker(ticker):
    results = get_data_by_ticker(ticker)
    assert results

def test_insert_data_mongo():
    data = [
        {"ticker": "SBER", "count": 1},
        {"ticker": "MAGN", "count": 1},
        {"ticker": "GAZP", "count": 1}
    ]
    insert_data_mongo(data)


@pytest.mark.parametrize("ticker", ("SBER",))
def test_get_aggr_volume_by_ticker(ticker):
    results = get_aggr_volume_by_ticker(ticker=ticker)
    assert results