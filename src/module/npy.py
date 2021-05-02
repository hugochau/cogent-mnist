"""
noy.py

Implements Npy
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import numpy as np

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