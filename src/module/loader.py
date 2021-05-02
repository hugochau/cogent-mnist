"""
loader.py

Implements Loader
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import numpy as np
from mlxtend.data import loadlocal_mnist

from config.constant import DATA_DIR


class Loader:
    """
    Defines function for loading mnist testing dataset
    """
    @staticmethod
    def load_mnist() -> np.ndarray:
        """
        Loads the MNIST dataset from byte-form local files into NumPy arrays

        Parameters
        ----------
        None

        Returns
        -------
        X:
            - MNIST test images
        y:
            - MNIST test lables
        """
        # set paths
        images_path = f'{DATA_DIR}/mnist/t10k-images-idx3-ubyte'
        labels_path = f'{DATA_DIR}/mnist/t10k-labels-idx1-ubyte'

        # load files
        X, y = loadlocal_mnist(images_path=images_path,
                               labels_path=labels_path)

        # ensuring numpy array type is uint8
        # TO DO dtype='float32' instead of dtype='uint8'
        X = X.astype('uint8')

        # reshaping to 28*28 pixels image
        # TO DO handle edge case
        # X.shape != (K, 784) where K > 0
        X = X.reshape((-1,28,28))

        return X, y