from database.connection import client, collection_aggr


def get_data_by_ticker(ticker: str):
    result = client.query(f"SELECT * FROM records WHERE sec_id='{ticker}'")
    return result.result_rows

def get_aggr_volume_by_ticker(ticker: str):
    query = f"""SELECT * FROM (SELECT toYear(trade_date) AS year, sec_id, sum(volume) as vol FROM moex.records
GROUP BY sec_id, year order by vol DESC, sec_id, year) as t WHERE sec_id='{ticker}'"""
    result = client.query(query)
    return result.result_rows

def insert_data_mongo(items: list[dict]):
    results = collection_aggr.insert_many(items)
    return results
