import numpy as np
import math


def tubular_cons(x):
    """
    :return: All cons should be minus than 0
    """
    sigma_y = 500  # 屈服应力σ y = 500  kgf/cm^2
    E = 0.85 * 10 ** 6  # 弹性模量E = 0.85 × 10^6kgf/cm^2
    p = 0.0025  # 密度 ρ=0.0025kgf/cm^3
    L = 250   # 柱子长度 L=250cm

    con1 = p / (math.pi * x[0] * x[1] * sigma_y) - 1
    con2 = 8 * p * L ** 2 / (math.pi ** 3 * E * x[0] * x[1] * (x[0] ** 2 + x[1] ** 2))
    con3 = 2.0 / x[0] - 1
    con4 = x[0] / 14 - 1
    con5 = 0.2 / x[1] - 1
    con6 = x[1] / 0.8 - 1

    return [con1, con2, con3, con4, con5, con6]


def tubular_obj(x):
    """
    :param x:
    2 <= x[0] <=14
    0.2 <= x[1] <= 0.8
    """

    return 9.82 * x[0]* x[1] + 2 * x[0]

