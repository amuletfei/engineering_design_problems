import numpy as np
import math

# I-beam design problem
def ibd_cons(x):
    """
    (x0,x1,x2,x3) = (h, b ,tw, tf)
    :return: All cons should be minus than 0
    """
    con1 = 2 * x[1] * x[2] + x[2] * (x[0] - 2 * x[3]) - 300
    con2 = (18 * x[0] * 10 ** 4) / (x[2] * (x[0] - 2 * x[3]) ** 3 + 2 * x[1] * x[2] * (4 * x[3] ** 2 + 3 * x[0] * (x[0] - 2 * x[3])))
    return [con1, con2]


def ibd_obj(x):
    """
    :param x:
    10 <= x[0] <= 80
    10 <= x[1] <= 50
    0.9 <= x[2] <= 5
    0.9 <= x[3] <= 5
    """
    return 5000 / (((x[2] * (x[0] - 2 * x[3])) / 12) + (x[1] * x[3] ** 3 / 6) + 2 * x[1] * x[3] * ((x[0] - x[3]) / 2) ** 2)