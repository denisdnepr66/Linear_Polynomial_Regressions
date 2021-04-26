import matplotlib.pyplot as plt
from functools import reduce
import math


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
    sum_of_x_y = reduce(lambda acc, next: acc + (next[0] * next[1]), zip(y, X), 0)
    sum_of_x = reduce(lambda acc, next: acc + next, X, 0)
    sum_of_x_squared = reduce(lambda acc, next: acc + (next * next), X, 0)
    squared_sum_of_x = sum_of_x * sum_of_x
    sum_of_y = reduce(lambda acc, next: acc + next, y, 0)

    m = (n * sum_of_x_y - sum_of_x * sum_of_y) / (n * sum_of_x_squared - squared_sum_of_x)
    b = (sum_of_y - m * sum_of_x) / n

    plt.plot([x for x in range(math.floor(min(X)), math.ceil(max(X)) + 1)], [
        m * x + b for x in range(math.floor(min(X)), math.ceil(max(X)) + 1)])
    plt.plot(X, y, 'b*')
    plt.show()
