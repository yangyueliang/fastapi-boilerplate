import time

from motor import motor_asyncio
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import Depends, FastAPI
from .logger import logger

app = FastAPI()

es = AsyncElasticsearch()
client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)


@app.middleware("http")
async def log_access(request, call_next):
    start_time = time.time()
    resp = await call_next(request)
    process_time = int((time.time() - start_time) * 1000)
    logger.bind(access=True).info(f"{request.url.path}\t{request.query_params}\t{resp.status_code}\t{process_time}")
    return resp


@app.get("/status")
async def root():
    return {"status": "ok"}


@app.get("/test/mongo")
async def test_mongo():
    pass


@app.get("/test/es")
async def test_es():
    return await es.search(
        index="documents",
        body={"query": {"match_all": {}}},
        size=20,
    )


if __name__ == "__main__":
    uvicorn.run(app=app, workers=1)
