def rcbd_cons(x):
    """
    :return: All cons should be minus than 0
    """
    con1 = x[1] / x[2] - 4
    con2 = 180 + 7.375 * x[0] ** 2 / x[2] - x[0] * x[1]
    return [con1, con2]


def rcbd_obj(x):
    """
    :param x:
    0 <= x[0], x[1] <= 1,
    5 <= x[2] <= 10
    """
    return 2.9*x[0] + 0.6*x[1]*x[2]
