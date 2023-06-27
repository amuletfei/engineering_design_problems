import numpy as np


def cbd_cons(x):
    """
    :return: All cons should be minus than 0
    """
    con1 = 61./x[0]**3 + 37./x[1]**3 + 19./x[2]**3 + 7./x[3]**3 + 1./x[4]**3 - 1
    return [con1]


def cbd_obj(x):
    """
    :param x:
    0.01 <= x[0],x[1],x[2],x[3],x[4] <= 100
    """
    return 0.0624 * np.sum(x)