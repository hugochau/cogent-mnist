"""
main.py

Defines Cogent MNIST API and CLI script
"""


__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import numpy as np

from module.png import Png
from module.npy import Npy
from module.generator import Generator
from module.parser import Parser
from util.util import get_spacing, log_item


def generate_numbers_sequence(digits, spacing_range, image_width):
    """
    Generates an image that contains the sequence of given numbers, spaced
    randomly using a uniform distribution.

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
    # compute randomg uniform spacing
    spacing = get_spacing(digits,
                          image_width,
                          spacing_range[0])

    # generate and return image
    gen = Generator(digits, spacing, image_width)
    image = gen.generate()

    return image


@log_item # log decorator
def main():
    """
    Main function for the cogentmnist app

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # parse args
    args = Parser.parse()

    # generate numbers sequence
    image = generate_numbers_sequence(args['sequence'],
                                      args['spacing_range'],
                                      args['image_width'])

    # save image as ndarray
    Npy.save(image)

    # save image as png
    Png.save(image)


if __name__ == '__main__':
    main()