import numpy as np


def wbd_cons(x):
    """
    :return: All cons should be minus than 0
    σ max = 30000,
    P = 6000 lb,
    L = 14 in.,
    δ max = 0.25 in.,
    E = 3×10^6 pis
    τ max = 13600 psi
    G = 1.2×10^7 psi
    """

    xichma_max = 30000
    p = 6000
    l = 14
    delta_max = 0.25
    e = 3 * 10 ** 6
    t_max = 13600
    g = 1.2 * 10 ** 7

    jj = 2 * np.sqrt(2) * x[0] * x[1] * (x[1] ** 2 / 4 + ((x[0] + x[2]) / 2) ** 2)
    R = np.sqrt(x[1] ** 2 / 4 + (x[0] + x[2]) ** 2 / 4)
    M = p * (l + x[1] / 2)
    tau2 = M * R / jj
    tau1 = p / (np.sqrt(2) * x[0] * x[1])
    tau = np.sqrt(tau1 ** 2 + 2 * tau1 * tau2 * x[1] / (2 * R) + tau2 ** 2)
    xichma_z = 6 * p * l / (e * x[2] ** 2 * x[3])
    theta_z = 6 * p * l ** 3 / (e * x[2] ** 2 * x[3])
    pc = 4.013 * e * np.sqrt(x[2] ** 2 * x[3] ** 6 / 36) / l ** 2 * (
                1 - x[2] * np.sqrt(e / (4 * g)) / (2 * l))

    con1 = tau - t_max
    con2 = xichma_z - xichma_max
    con3 = theta_z - delta_max
    con4 = x[0] - x[3]
    con5 = p - pc
    con6 = 0.125 - x[0]
    con7 = 1.10471 * x[0]**2 + 0.04811 * x[2]*x[3]*(14 + x[1]) - 5

    return [con1, con2, con3, con4, con5, con6, con7]


def wbd_object(x):
    """
    :param x:
    0.1 <= x[0] <= 2,
    0.1 <= x[1] <= 10,
    0.1 <= x[2] <= 10,
    0.1 <= x[3] <= 2
    :return:
    """

    return 1.10471 * x[0]**2 * x[1] + 0.04811 * x[2] * x[3] * (14 + x[1])
