"""
_formatter.py

Fixes logging.Formatter misbehavior when calling
functions outside of their original location
"""


__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import logging


class _Formatter(logging.Formatter):
    """
    The logging decorator logs the file and function name
    of the function it decorates.
    It should log the called function name instead.
    _Formatter corrects this behavior.

    As an example, say we have the following function
    Also assume sub_main throws an error

        @log_item
        def main:
            sub_main

    Without _Formatter, log should look like:

    INFO - main.py - __main__.main - begin function
    ERROR - main.py - __main__.main - exception: name 'aaa' is not defined

    Without _Formatter, log should look like:

    INFO - submain.py - __main__.main - begin function
    ERROR - submain.py - __main__.main - exception: name 'aaa' is not defined
    """

    def format(self, record):
        """
        Abstract
        ----------
        Takes record as input, replaces funcName and filename
        with override values if existing.

        Parameters
        ----------
        record:
            - Data saved to .png

        Returns
        -------
        None
        """
        # func/filename override defined in log_item.py
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override

        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override

        # returns superclass original method
        # but with updated record attributes
        return super(_Formatter, self).format(record)