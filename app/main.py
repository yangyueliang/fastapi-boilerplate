import time

import uvicorn
from fastapi import Depends, FastAPI
from .logger import logger

app = FastAPI()


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


if __name__ == "__main__":
    uvicorn.run(app=app, workers=1)
