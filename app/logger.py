import os

from loguru import logger

_BASE_DIR = "logs"
if not os.path.exists(_BASE_DIR):
    os.mkdir(_BASE_DIR)

logger.add(os.path.join(_BASE_DIR, 'server.log'), rotation="00:00", retention="5 days")
logger.add(os.path.join(_BASE_DIR, 'access.log'), rotation="00:00", retention="5 days",
           filter=lambda record: "access" in record["extra"])
