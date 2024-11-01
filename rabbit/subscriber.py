from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue
from loguru import logger

from config.settings import settings
from database.query import get_aggr_volume_by_ticker, insert_data_mongo
from schemas import Volume

broker = RabbitBroker(url=settings.rabbit_url)
app = FastStream(broker)


@broker.subscriber(RabbitQueue(name=settings.queue_tasks, durable=True))
async def task(ticker: str):
    logger.info(f"Start ticker {ticker}")
    result = get_aggr_volume_by_ticker(ticker=ticker)
    data = []
    for item in result:
        try:
            volume = Volume(
                year=item[0],
                sec_id=item[1],
                volume=item[2]
            )
        except Exception as e:
            logger.error(e)
            continue
        data.append(volume.model_dump())
    if data:
        insert_data_mongo(items=data)
        logger.success(f'Write {len(data)} items')
    logger.success(f"Task End")
