"""
noy.py

Implements Npy
"""

__version__ = '0.1'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from config.constant import DATA_DIR


class Npy:
    """
    Defines read/write functions for npy files
    """
    @staticmethod
    def save(image: np.ndarray) -> None:
        """
        Abstract
        ----------
        Saves image to .npy file

        Parameters
        ----------
        image:
            - Image data

        Returns
        -------
        None
        """
        # save image as ndarray
        np.save(f'{DATA_DIR}/output/image', image)


    @staticmethod
    def open(filepath) -> np.ndarray:
        """
        Abstract
        ----------
        Opens .npy file

        Parameters
        ----------
        filepath:
            - path to .npy file
            - can be either absolute or relative

        Returns
        -------
        nd:
            - File data
        """
        # load image as ndarray
        nd = np.load(filepath)

        return nd