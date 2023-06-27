def penalty_fuc(x, cons, k):
    pen_temp = 0
    for i in range(len(cons)):
        if cons[i] > 0:
            pen_temp += k[i] * x[i] ** 2
    return pen_temp

