import numpy as np


def pvd_cons(x):
    """
    :return: All cons should be minus than 0
    """
    con1 = -x[0] + 0.0193 * x[2]
    con2 = -x[1] + 0.00954 * x[2]
    con3 = -np.pi * x[2] ** 2 * x[3] - 4 / 3 * np.pi * x[2] ** 3 + 1296000
    con4 = x[3] - 240
    return [con1, con2, con3, con4]


def pvd_obj(x):
    """
    :param x:
    0 <= X[0] <= 99,
    0 <= X[1] <= 99,
    10 <= X[2] <= 200,
    10 <= X[3] <= 200
    :return:
    """
    return 0.6224 * x[0] * x[2] * x[3] + 1.7781 * x[1] * x[2] ** 2 + 3.1661 * x[0] ** 2 * x[3] + 19.84 * x[0] ** 2 * x[2]
