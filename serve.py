import uvicorn
from fastapi import FastAPI


from routers.moex import moex_router

app = FastAPI()

app.include_router(moex_router, prefix="/moex")


if __name__ == "__main__":
    uvicorn.run("serve:app", host="127.0.0.1", port=5000, reload=True)
