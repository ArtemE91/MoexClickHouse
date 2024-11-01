from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

from config.settings import settings


broker = RabbitBroker(url=settings.rabbit_url)
app = FastStream(broker)


@broker.subscriber(RabbitQueue(name="tasks", durable=True))
async def task(ticker: str):
    print(ticker)
