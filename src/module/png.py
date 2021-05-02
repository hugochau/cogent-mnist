"""
png.py

Implements Png
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import numpy as np
from PIL import Image

from config.constant import DATA_DIR


class Png:
    """
    Defines functions for manipulating png files
    """
    @staticmethod
    def save(image: np.ndarray) -> None:
        """
        Abstract
        ----------
        Saves image to .png

        Parameters
        ----------
        image:
            - The image, represented as a numpy array

        Returns
        -------
        None
        """
        # load image using PIL
        img = Image.fromarray(image, 'L')

        # save as .png under data/output
        img.save(f'{DATA_DIR}/output/image.png')
