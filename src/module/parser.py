"""
parser.py

Implements Parser
"""

__version__ = '0.1'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import argparse

from util.util import validate_int


class Parser:
    """
    Defines function for parsing and validating CLI arguments
    """
    @staticmethod
    def parse() -> dict:
        """
        Abstract
        ----------
        Parse and validate CLI arguments

        Parameters
        ----------
        None

        Returns
        -------
        dict:
            - validated CLI arguments in a dictionary

        """
        # define parser
        parser = argparse.ArgumentParser(description='CLI arguments parser for cogentmnist app')

        # parse arguments
        parser.add_argument('sequence',
                            help='the sequence of digits to be generated. ex: "0 1 2 3"')
        parser.add_argument('min_spacing',
                            type=int,
                            help='minimum spacing between consecutive digits. ex: 1')
        parser.add_argument('max_spacing',
                            type=int,
                            help='maximum spacing between consecutive digits. ex: 10')
        parser.add_argument('image_width',
                            type=int,
                            help='width of the generated image. ex: 128')
        args = parser.parse_args()

        # combine arguments into a dictionary
        # using util function validate_int to validate numbers
        # must be strictly positive
        dict = {}
        dict['sequence'] = [int(item) for item in args.sequence.split(',')]
        dict['spacing_range'] = (
            validate_int(args.min_spacing),
            validate_int(args.max_spacing)
        )
        dict['image_width'] = validate_int(args.image_width)

        # raise ValueError if max_spacing < min_spacing
        if not dict['spacing_range'][1] > dict['spacing_range'][0]:
            raise ValueError(f'max_spacing {dict["spacing_range"][1]} must be greater or equal'
                             + f'to min_spacing {dict["spacing_range"][0]}')

        return dict
