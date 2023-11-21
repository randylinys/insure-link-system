# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('logger')
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

os.makedirs('logs', exist_ok=True)
handler = RotatingFileHandler('logs/log', maxBytes=10**5, backupCount=10)
handler.setFormatter(formatter)

logger.addHandler(handler)
