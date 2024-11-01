from faststream.rabbit import RabbitBroker

from config.settings import settings


broker = RabbitBroker(url=settings.rabbit_url)

async def publish_task_ticker(ticker: str):
    async with broker as br:
        await br.publish(ticker, settings.queue_tasks)
