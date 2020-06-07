import os
import json
import numpy as np


class Volume:
    def __init__(self, path, dtype=np.int16, info_path=None):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Couldn't find Volume at {path}")
        if info_path:
            if not os.path.exists(info_path):
                raise FileNotFoundError(f"Couldn't find Volume info at {info_path}")
            self.info = self.read_volume_info(info_path)
        if not self.info:
            self.info = None

        self.data = self.read_volume_data(path, dtype)

    @staticmethod
    def read_volume_data(path, dtype):
        volume_data = np.fromfile(path, dtype)
        return volume_data

    @staticmethod
    def read_volume_info(path):
        with open(path) as volume_info_file:
            volume_info = json.load(volume_info_file)
            return volume_info

    def instance_check(self, other):
        if not isinstance(other, np.ndarray):
            raise NotImplementedError(f"Can add only numpy array to volume.data, but was of type {type(other)}")
        if self.data.shape != other.shape:
            raise ValueError(f"Dimension mismatch of noise ({self.data.shape}) and volume ({other.shape}).")

    def __add__(self, other):
        self.instance_check(other)
        return self.data + other

    def __mul__(self, other):
        self.instance_check(other)
        return self.data * other

    def __pow__(self, power: float):
        return self.data ** power
