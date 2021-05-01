"""
util.py

Implements util functions
"""


__version__ = '0.1'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import sys
import os
import functools
from random import choice
from inspect import getframeinfo, stack
import numpy as np

from module.logger import Logger


def log_item(func):
    """
    Log decorator

    Parameters
    ----------
    func:
        - decorated function

    Returns
    -------
    wrapper:
        - function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = Logger().logger # get a logger

        # # creating a list of positional args
        # # repr() is similar but more precise than str()
        # args_str = [repr(a) for a in args]
        # # creating a list of keyword args
        # # f-string formats each arg as key=value
        # # where the !r specifier means that repr()
        # # is used to represent the value
        # kwargs_str = [f"{k}={v!r}" for k, v in kwargs.items()]
        # basic_args = ", ".join(args_str + kwargs_str)

        # generate file/function name for calling functions
        # __func.name__ will give the name of the caller function
        # ie. wrapper and caller file name ie log_item.py
        # using extra param to get the actual function name
        # by leveraging inspect.getframeinfo
        pyfile = getframeinfo(stack()[1][0])
        extra_args = {
            'func_name_override': f'{func.__globals__["__name__"]}.{func.__name__}',
            'file_name_override': os.path.basename(pyfile.filename)
        }

        logger.info(f"begin function", extra=extra_args)
        try:
            value = func(*args, **kwargs)
            if value:
                logger.info(f"end function, returned {value!r}", extra=extra_args)
            else:
                logger.info(f"end function, no return", extra=extra_args)

            return value
        except:
            # log error if fails and raise
            logger.error(f"exception: {str(sys.exc_info()[1])}", extra=extra_args)
            raise

    return wrapper


def classify_labels(labels: np.ndarray) -> list:
    """
    Classify MNIST labels by value

    Parameters
    ----------
    labels:
        - MNIST testing labels

    Returns
    -------
    sorted_labels:
        - labels sorted by value
    """
    #
    sorted_labels = [[] for i in range(10)]

    #
    for i in range(len(labels)):
        sorted_labels[labels[i]].append(i)

    return sorted_labels


def get_spacing(
        sequence: list,
        image_width: int,
        min_spacing: int,
        digit_width:int = 28) -> int:
    """
    Generates a spacing interval between two consecutive digits
    Follows a uniformed distribution

    Parameters
    ----------
    sequence:
        - A list-like containing the numerical values of the digits from which
            the sequence will be generated (for example [3, 5, 0])
    image_width:
        - Digits sequence width
    min_spacing:
        - Represents the min spacing between digits
        - Unit should be pixel.
    digit_width:
        - default 28

    Returns
    -------
    spacing:
        - Specifies the width of the MNIST digits
        - Unit should be pixel.
    """
    if len(sequence) == 1:
        theo_spacing = 0 # no spacing required in this case
    else:
        # derived from formula
        # image_width = (len(sequence) * digit_width) + theo_spacing/(len(sequence) - 1)
        theo_spacing = (image_width - len(sequence) * digit_width) / (len(sequence) - 1)

    # raise ValueError if theo_spacing not inside spacing_range
    if not theo_spacing > min_spacing:
            raise ValueError(f'uniform spacing {int(theo_spacing)} '
                             + f'must be greater than {min_spacing}')

    # pick random value for range [min_spacing, theo_spacing]
    spacing = choice([i for i in range(min_spacing, int(theo_spacing))])

    return spacing

def validate_int(arg: int):
    """
    Abstract
    ----------
    Checks if arg input is strictly positive 

    Parameters
    ----------
    arg:
        - parsearg argument that needs validation 

    Returns
    -------
    arg:
        - validated parsearg argument

    """
    if not arg > 0:
        raise ValueError("Must be strictly positive")

    return arg