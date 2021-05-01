"""
test.py

Implements testing functions
"""


__version__ = '0.1'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

from module import *
from util.util import *


def test_loader_load_mnist():
    """
    Abstract
    ----------
    Testing module.loader.load_mnist function
    """
    img, lbl = Loader.load_mnist()

    return img, lbl


def test__pil_save():
    """
    Abstract
    ----------
    Testing module.loader.load_mnist function
    """
    # load img
    img, lbl = Loader.load_mnist()

    # save img
    _pil._Pil.save(img[7])


def test_parser_parse():
    """
    Abstract
    ----------
    Testing module.parser.parse function
    """
    args = Parser.parse()


def test_get_spacing():
    """
    Abstract
    ----------
    Testing util.get_spacing function
    """
    sequence = [1,2,3,4]
    width = 136
    print(get_spacing(sequence, width))


def test_classify_labels():
    """
    Abstract
    ----------
    Testing util.get_spacing function
    """
    img, lbl = Loader.load_mnist()
    sorted_labels = classify_labels(lbl)

    for i in sorted_labels[9]:
        print(lbl[i])


def test_generator_generate():
    """
    Abstract
    ----------
    Testing module.parser.parse function
    """
    sequence = [7,8,4,2]
    width = 150
    gen = generator.Generator(sequence, width)
    image = gen.generate()
    pil._Pil.save(image)


def test_npy_save():
    """
    Abstract
    ----------
    Testing module.parser.parse function
    """
    sequence = [7,8,4,2]
    width = 150
    gen = generator.Generator(sequence, width)
    image = gen.generate()
    npy.Npy.save(image)


def test_npy_load():
    """
    Abstract
    ----------
    Testing module.parser.parse function
    """
    nd = npy.Npy.open('image.npy')


if __name__ == '__main__':
    test_npy_load()