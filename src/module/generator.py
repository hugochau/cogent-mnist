"""
generator.py

Implements Generator
"""


__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

from random import choice

import numpy as np

from module.loader import Loader
from util.util import classify_labels


class Generator():
    """
    Implements cogentapp main function e.g., generator()
    """
    def __init__(self, sequence: list, spacing: int, width: int):
        """
        Class instantiation

        Parameters
        ----------
        sequence:
            - A list-like containing the numerical values of the digits from which
            the sequence will be generated (for example [3, 5, 0])
        spacing:
            - Uniform spacing between two consecutive images in the sequence
        width:
            - Digits sequence width

        Returns
        -------
        Generator object with following attributes

        images:
            - MNIST testing images
        labels:
            - MNIST testing labels
        sequence:
            - A list-like containing the numerical values of the digits from which
            the sequence will be generated (for example [3, 5, 0])
        width:
            - Digits sequence width
        height:
            - Digits sequence height
            - Default to 28 e.g., identical to the height of the MNIST input digits
        spacing:
            - Uniform spacing between two consecutive images in the digits sequence
        """
        self.images, self.labels = Loader.load_mnist()
        self.sequence = sequence
        self.width = width
        self.height = 28
        self.spacing = spacing


    def generate(self):
        """
        Generate an image that contains the sequence of given numbers, spaced
        randomly using an uniform distribution.

        Adapted from https://github.com/ankitaggarwal011/MNIST-Sequence/

        Parameters
        ----------
        digits:
            - A list-like containing the numerical values of the digits from which
            the sequence will be generated (for example [3, 5, 0]).
        spacing_range:
            - a (minimum, maximum) pair (tuple), representing the min and max spacing
            between digits. Unit should be pixel.
        image_width:
            - specifies the width of the image in pixels.

        Returns
        -------
        image:
            - The image containing the sequence of numbers. Images should be represented
            as floating point 32bits numpy arrays with a scale ranging from 0 (black) to
            1 (white), the first dimension corresponding to the height and the second
            dimension to the width.
        """
        spacing = np.ones(self.height * self.spacing,
                          dtype='uint8').reshape(self.height,
                                                 self.spacing)
        spacing *= 0 # black blackround

        sorted_labels = classify_labels(self.labels)
        idx = choice(sorted_labels[self.sequence[0]])
        image = self.images[idx]

        for i in range(1, len(self.sequence)):
            if i < len(self.sequence):
                image = np.hstack((image, spacing))

            idx = choice(sorted_labels[self.sequence[i]])
            image = np.hstack((image, self.images[idx]))

        # remaining spacing to get actual image width
        remain = self.width - image.shape[1]
        spacing = np.ones(self.height * remain,
                          dtype='uint8').reshape(self.height,
                                                 remain)
        spacing *= 0 # black blackround
        image = np.hstack((image, spacing))

        return image
