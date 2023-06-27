import numpy as np


L = 240
M_max = 1.8 * 10 ** 6
P = 1500
Q = 10000
theta = np.pi / 4


def pld_cons(x):
    """
    :return: All cons should be minus than 0
    """
    L1 = np.sqrt((x[3] - x[1]) ** 2 + x[0] ** 2)
    L2 = np.sqrt((x[3] * np.sin(theta) + x[0]) ** 2 + (x[1] - x[3] * np.cos(theta)) ** 2)
    R = np.abs(-x[3] * (x[3] * np.sin(theta) + x[0]) + x[0] * (x[1] - x[3] * np.cos(theta))) / np.sqrt((x[3] - x[1]) ** 2 + x[0] ** 2)
    F = np.pi * P * x[2] ** 2 / 4
    con1 = Q * L * np.cos(theta) - R * F
    con2 = Q * (L - x[3]) - M_max
    con3 = 1.2 * (L2 - L1) - L1
    con4 = x[2] / 2 - x[1]
    return [con1, con2, con3, con4]


def pld_obj(x):
    """
    :param x:
    0.05 <= X[0] <= 500,
    0.05 <= X[1] <= 500,
    0.05 <= X[2] <= 120,
    0.05 <= X[3] <= 500
    """
    L1 = np.sqrt((x[3] - x[1]) ** 2 + x[0] ** 2)
    L2 = np.sqrt((x[3] * np.sin(theta) + x[0]) ** 2 + (x[1] - x[3] * np.cos(theta)) ** 2)
    return 0.25*np.pi*x[2]**2 * (L2 - L1)