import numpy as np
#import cv2
import re
reg = re.compile(r'^(\d+)\s(\d+)\s$')

HEADER_SIZE = len('PF\n')
LENDIAN_SIZE = len('{:f}\n'.format(-1))
BENDIAN_SIZE = len('{:f}\n'.format(1))


class PFMLoader:
    def __init__(self, dim, color, endian='<'):
        self.width, self.height = dim
        self.color = color
        self.endian = endian
        self.dim_size = len('{0} {1}\n'.format(self.width, self.height))
        if endian == '<':
            self.data_size = HEADER_SIZE + self.dim_size + LENDIAN_SIZE
        else:
            self.data_size = HEADER_SIZE + self.dim_size + BENDIAN_SIZE
        self.shape = (self.height, self.width, 3) if self.color else (self.height, self.width, 1)

        print(self.data_size)

    def load_pfm(self, path):
        data = np.fromfile(path, self.endian + 'f', offset=self.data_size)
        data = np.reshape(data, self.shape)
        return data
