import clickhouse_connect

from config.settings import settings


client = clickhouse_connect.get_client(**settings.clickhouse.model_dump())
