import clickhouse_connect
from pymongo import MongoClient

from config.settings import settings


client = clickhouse_connect.get_client(**settings.clickhouse.model_dump())

client_mongo = MongoClient()
db = client_mongo["moex"]
collection_aggr = db["aggregate"]
