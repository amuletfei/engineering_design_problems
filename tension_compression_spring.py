def csd_cons(x):
    """
    :return: All cons should be minus than 0
    """
    con1 = 1 - (x[1] ** 3 * x[2]) / (71785 * x[0] ** 4)
    con2 = (4 * x[1] ** 2 - x[0] * x[1]) / (12566 * (x[1] * x[0] ** 3 - x[0] ** 4)) + 1 / (5108 * x[0] ** 2) - 1
    con3 = 1 - 140.45 * x[0] / (x[1] ** 2 * x[2])
    con4 = (x[0] + x[1]) / 1.5 - 1
    # print('cons', con1, con2, con3, con4)
    return [con1, con2, con3, con4]


def csd_obj(x):
    """
    :param x:
    0.05 <= X[0] <= 2,
    0.25 <= X[1] <= 1.3,
    2 <= X[2] <= 15
    :return:
    """
    return (x[2] + 2) * x[1] * x[0] ** 2


