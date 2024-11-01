from fastapi import APIRouter

from rabbit.publisher import publish_task_ticker

moex_router = APIRouter(tags=["Moex"])

@moex_router.get("/{ticker}")
async def retrieve_all_records(ticker: str) -> dict:
    await publish_task_ticker(ticker=ticker)
    return {"message": "the ticker has been successfully added to the queue"}


