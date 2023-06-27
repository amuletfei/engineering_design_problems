import numpy as np


# Corrugated Bulkhead Problem
def cbhd_cons(x):
    """
    [x1, x2, x3, x4] = [width, depth, length, thickness]
    :return: All cons should be minus than 0
    """
    con1 = -x[3] * x[2] * (0.4 * x[0] + x[2] / 6) + 8.94 * (x[0] + np.sqrt(np.abs(x[2] ** 2 - x[1] ** 2)))
    con2 = -x[3] * x[1] ** 2 * (0.2 * x[0] + x[2] / 12) + 2.2 * (8.94 * (x[0] + np.sqrt(np.abs(x[2] ** 2 - x[1] ** 2)))) ** (4. / 3)
    con3 = -x[3] + 0.0156 * x[0] + 0.15
    con4 = -x[3] + 0.0156 * x[2] + 0.15
    con5 = -x[3] + 1.05
    con6 = -x[2] + x[1]
    return [con1, con2, con3, con4, con5, con6]


def cbhd_obj(x):
    """
    :param x:
    0.05 <= X[0] <= 500,
    0.05 <= X[1] <= 500,
    0.05 <= X[2] <= 120,
    0.05 <= X[3] <= 500
    """
    return 5.885*x[3]*(x[0] + x[2]) / (x[0] + np.sqrt(np.abs(x[2]**2 - x[1]**2)))
