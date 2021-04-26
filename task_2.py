import matplotlib.pyplot as plt
from functools import reduce
import math
import numpy as np
from numpy.linalg import inv


for i in range(1, 16):
    file = open("data/dane{}.txt".format(i), "r")
    X = []
    y = []

    for x in file:
        point = x.split(" ")
        point.remove('\n')
        X.append(float(point[0]))
        y.append(float(point[1]))

    n = len(X)
    sum_of_x_4 = reduce(lambda acc, next: acc + pow(next, 4), X, 0)
    sum_of_x_3 = reduce(lambda acc, next: acc + pow(next, 3), X, 0)
    sum_of_x_2 = reduce(lambda acc, next: acc + pow(next, 2), X, 0)
    sum_of_x = reduce(lambda acc, next: acc + next, X, 0)
    sum_of_y = reduce(lambda acc, next: acc + next, y, 0)
    sum_of_xy = reduce(lambda acc, next: acc + next[0] * next[1], zip(X, y), 0)
    sum_of_x2_y = reduce(lambda acc, next: acc + pow(next[0], 2) * next[1], zip(X, y), 0)

    m1 = np.array([
        [sum_of_x_4, sum_of_x_3, sum_of_x_2],
        [sum_of_x_3, sum_of_x_2, sum_of_x],
        [sum_of_x_2, sum_of_x, n]
    ])

    m2 = np.array([
        sum_of_x2_y,
        sum_of_xy,
        sum_of_y
    ])

    params = inv(m1).dot(m2)

    plt.plot([x for x in range(math.floor(min(X)), math.ceil(max(X)) + 1)], [
        params[0] * x * x + params[1] * x + params[2] for x in range(math.floor(min(X)), math.ceil(max(X)) + 1)])
    plt.plot(X, y, 'b*')
    plt.show()
