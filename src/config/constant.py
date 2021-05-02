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


# Data directory
DATA_DIR = f'./data'

# Logger constants
LOG_LEVEL = logging.INFO
LOG_FILENAME = 'log_' \
                + datetime.datetime.isoformat(datetime.datetime.today())
LOG_FILEPATH = os.path.join(f'./data/log', LOG_FILENAME)
