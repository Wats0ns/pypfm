import numpy as np
import sys
sys.path.append('.')
from pypfm import PFMLoader
from pyzfp import decompress

def test_save_and_load():
    shape = (2, 3)
    data = np.random.rand(shape[0], shape[1], 1).astype('float32')
    loader = PFMLoader((shape[1], shape[0]), False, compress=False)

    loader.save_pfm('test.pfm', data)
    res = loader.load_pfm('test.pfm')
    assert np.array_equal(res, data)

def test_save_and_load_no_size():
    shape = (2, 3)
    data = np.random.rand(shape[0], shape[1], 1).astype('float32')
    loader = PFMLoader(color=False, compress=False)

    loader.save_pfm('test.pfm', data)
    res = loader.load_pfm('test.pfm')
    assert np.array_equal(res, data)


def test_save_and_load_with_compression():
    import pypfm
    print(pypfm.__version__)
    shape = (2, 3)
    data = np.random.rand(shape[0], shape[1], 1).astype('float32')
    loader = PFMLoader((shape[1], shape[0]), False, compress=True)

    saved = loader.save_pfm('test_.pfm', data)
    res = loader.load_pfm('test_.pfm')
    # assert np.array_equal(saved, res)
    # res = decompress(np.ascontiguousarray(saved, dtype=np.uint8), data.shape, np.dtype('float32'), tolerance=0.5,
    #            parallel=False)
    error = np.abs((res - data))
    mean_error = np.mean(error)
    relative_error = np.mean(error /np.abs(data))
    print(error)
    print(res)
    print(mean_error, relative_error)
    # q
    assert relative_error < 0.5


def test_clean():
    test = np.asarray([[1, 4], [4, 3], [6, 4]])
    placeholder = 0
    res = PFMLoader().clean_values(test, [2, 5], 0)
    assert np.array_equal(res[0], np.asanyarray([[placeholder, 4], [4, 3], [placeholder, 4]]))
    assert res[1] == 2
