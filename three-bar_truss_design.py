import numpy as np


L = 100
P = 2
xichma = 2


def tbtd_cons(x):
    """
    :return: All cons should be minus than 0
    """
    con1 = (np.sqrt(2) * x[0] + x[1]) / (np.sqrt(2) * x[0] ** 2 + 2 * x[0] * x[1]) * P - xichma
    con2 = x[1] * P / (np.sqrt(x[0] ** 2 + 2 * x[0] * x[1])) - xichma
    con3 = P / (np.sqrt(2) * x[1] + x[0]) - xichma
    return [con1, con2, con3]


def tbtd_obj(x):
    """
  :param x:
  1 <= x[0] <= 1
  0 <= x[1] <= 1
  """
    return (2*np.sqrt(2)*x[0] + x[1]) * L