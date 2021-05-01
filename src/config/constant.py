"""
constant.py
Store constants here
"""


__version__ = '1,0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import logging
import datetime
import os
from pathlib import Path


# Data directory
# d = Path().resolve().parent
DATA_DIR = f'./data'

# Logger
LOG_LEVEL = logging.INFO
LOG_FILENAME = 'log_' \
                + datetime.datetime.isoformat(datetime.datetime.today())
LOG_FILEPATH = os.path.join(f'./data/log', LOG_FILENAME)
