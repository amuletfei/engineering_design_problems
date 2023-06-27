import numpy as np


def sd_obj(x):
    """
    :param x:
    12 <= x[0] <= 1,
    12 <= x[2] <= 2,
    12 <= x[3] <= 3,
    12 <= x[4] <= 4
    """
    return ((1 / 6.931) - ((x[2]*x[1]) / (x[0] * x[3]))) ** 2
