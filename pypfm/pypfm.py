import numpy as np
import sys
import re
from pyzfp import compress, decompress
reg = re.compile(r'^(\d+)\s(\d+)\s$')

HEADER_SIZE = len('PF\n')
LENDIAN_SIZE = len('{:f}\n'.format(-1))
BENDIAN_SIZE = len('{:f}\n'.format(1))


class PFMLoader:
    def __init__(self, dim=None, color=True, endian='<', compress=False):
        self.width, self.height = dim
        self.color = color
        self.endian = endian
        self.dim_size = len('{0} {1}\n'.format(self.width, self.height))
        if endian == '<':
            self.data_size = HEADER_SIZE + self.dim_size + LENDIAN_SIZE
        else:
            self.data_size = HEADER_SIZE + self.dim_size + BENDIAN_SIZE
        self.shape = (self.height, self.width, 3) if self.color else (self.height, self.width, 1)
        self.compress = compress
        print(self.data_size)

    def load_pfm(self, path):
        data = np.fromfile(path, offset=self.data_size, dtype=np.uint8 if self.compress else self.endian + 'f')
        # return data
        # print('At load: ', self.shape, data.dtype, np.ascontiguousarray(data, dtype=np.dtype('uint8').shape))
        if self.compress:
            data = decompress(np.ascontiguousarray(data, dtype=np.uint8), self.shape, np.dtype('float32'), tolerance=0.5, parallel=False)
            return data
        data = np.reshape(data, self.shape)
        return data

    def save_pfm(self, path, image, scale=1):
        if image.dtype.name != 'float32':
            raise ValueError('Image dtype must be float32.')

        color = self.color
        endian = image.dtype.byteorder
        if endian == '<' or endian == '=' and sys.byteorder == 'little':
            scale = -scale
        shape = image.shape
        if self.compress:
            image = np.ascontiguousarray(compress(image, tolerance=0.5, parallel=False), dtype=np.uint8)
        with open(path, 'w') as file:
            file.write('PF\n' if color else 'Pf\n')
            file.write('%d %d\n' % (shape[1], shape[0]))
            file.write('%f\n' % scale)
            image.tofile(file)
        return image

