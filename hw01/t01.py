import numpy as np
import matplotlib.pyplot as plt
from math import factorial

eps = 10 ** (-6)

""" 1A
eps = 10^(-6), 1 / (k^2 - k - z) <= 1 / k^1.9 <=> k^1.9 <= k^2 - k - z (с какого-то k)
 => k^1.9 + k + z <= k^2 с какого-то k
 поэтому оценим интегралом int_n^inf{1 / k^1.9} = 10 / (9 * n^(9/10)) = eps
 <=> n <= 5218052
"""


def w_A(z):
    n = 5218052
    res = 0
    for k in range(1, n + 1):
        res += 1 / (k ** 2 - k - z)
    return res


def taskA():
    data_x = []
    data_y = []
    step = 0.01
    z = 0 + step
    while z < 2:
        data_x.append(z)
        data_y.append(w_A(z))
        z += step
    plt.subplot(211)
    plt.title("Integral error estimation")
    plt.plot(data_x, data_y)
    plt.ylabel("w_A(z)")
    plt.xlabel("z")


"""
Модельный ряд: sum_1^inf{1 / (k^2)}. Очевидно, что сумма отношений стремится к единице.
sum_1^inf{1 / k^2} = pi^2 / 6 = s. 
Тогда надо посчитать s + sum_1^inf(1 / (k^2 - k - z) - 1 / k^2)
1 / (k^2 - k - z) - 1 / k^2 <= (k + z) / (k^2 * (k^2 - k - z)) =
= (1 + z / k) / (k * (k^2 - k - z)) <= 2 / k^2.9
Тогда оцениваем int_n^inf{2 / k^2.9} = 20 / (19 * n^(19/10)) = 10^(-6)
<=> n <= 1478
"""


def w_B(z):
    n = 1478
    res = np.pi ** 2 / 6
    for k in range(1, n + 1):
        res += 1 / (k ** 2 - k - z) - 1 / k ** 2
    return res


def taskB():
    data_x = []
    data_y = []
    step = 0.01
    z = 0 + step
    while z < 2:
        data_x.append(z)
        data_y.append(w_B(z))
        z += step
    plt.subplot(211)
    plt.title("Model series method")
    plt.plot(data_x, data_y)
    plt.ylabel("w_B(z)")
    plt.xlabel("z")


"""
просто посмотрим на w_A - w_B. 
очевидно он должен быть от -2 * eps до 2 * eps
"""


def taskC():
    data_x = []
    data_y = []
    step = 0.01
    z = 0 + step
    while z < 2:
        data_x.append(z)
        data_y.append(w_A(z) - w_B(z))
        z += step
    plt.subplot(211)
    plt.title("Difference between methods")
    plt.plot(data_x, data_y)
    plt.ylabel("w_A(z) - w_B(z)")
    plt.xlabel("z")


def main():
    plt.figure(1)
    #taskA()
    #taskB()
    taskC()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
