import logging
from logging.handlers import TimedRotatingFileHandler
from fastapi.logger import logger as applogger
from app.core import config


formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(filename)s - %(funcName)s - %(message)s")
handler = TimedRotatingFileHandler(config.LOGFILE, when='d',interval=1,backupCount=30)
handler.setFormatter(formatter)
logging.getLogger().setLevel(config.LOGLEVEL)
applogger.addHandler(handler)