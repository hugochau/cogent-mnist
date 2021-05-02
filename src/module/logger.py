"""
logger.py

Implements Logger
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import logging
import sys

from module._formatter import _Formatter
from config.constant import (
    LOG_FILENAME,
    LOG_FILEPATH,
    LOG_LEVEL
)


class Logger:
    """
    Defines a custom logger for the app
    """
    def __init__(self):
        """
        Class instantiation

        Parameters
        ----------
        None

        Returns
        -------
        Logger object with following attributes

        logger:
            - logging.Logger object
        """
        self.logger = Logger.get_logger()


    @staticmethod
    def get_logger() -> logging.Logger:
        """
        Builds a custom loggin.Logger object

        Parameters
        ----------
        None

        Returns
        -------
        logger:
            - logging.Logger object
        """
        # init logger
        logger = logging.Logger(LOG_FILENAME)
        logger.setLevel(LOG_LEVEL)

        # setting up stream logger
        stream_logger = logging.StreamHandler()
        # setting the _Formatter formatter type
        stream_logger.setFormatter(_Formatter)
        stream_logger.setFormatter(_Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
        ))
        # adding handlers
        logger.addHandler(stream_logger)

        # setting up file logger
        try:
            file_logger = logging.FileHandler(LOG_FILEPATH, 'a+')
        # raise error if file path not found
        except FileNotFoundError as e:
            sys.exit(e)
        file_logger.setFormatter(_Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
        ))
        logger.addHandler(file_logger)

        return logger
