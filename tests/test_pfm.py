import numpy as np
import sys
sys.path.append('.')
from pypfm import PFMLoader


def test_save_and_load():
    shape = (2, 3)
    data = np.random.rand(shape[0], shape[1], 1).astype('float32')
    loader = PFMLoader((shape[1], shape[0]), False)

    loader.save_pfm('test.pfm', data)
    res = loader.load_pfm('test.pfm')
    assert np.array_equal(res, data)