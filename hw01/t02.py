import matplotlib.pyplot as plt
import numpy as np


def s_eitken(z, n):
    s1 = z
    s2 = s1 + 1 / 3 * z ** 2
    s3 = s2 + 1 / 5 * z ** 3
    res = s3 - (s3 - s2) ** 2 / (s3 - s2 - s2 + s1)
    for k in range(4, n + 1):
        s1 = s2
        s2 = s3
        s3 += 1 / (2 * k - 1) * z ** k
        if s3 - s2 - s2 + s1 != 0:
            res = s3 - (s3 - s2) ** 2 / (s3 - s2 - s2 + s1)
    return res


def s(z):
    n = 10 ** 6
    res = 0
    for k in range(1, n + 1):
        res += 1 / (2 * k - 1) * z ** k
    return res


def calculate_value(z, wolfram_value):
    print("--s(" + str(z) + ")--")
    wolfram_value = wolfram_value
    eitken_value = s_eitken(z, 10 ** 3)
    print("wolfram: " + str(wolfram_value))
    print("eitkens method: " + str(eitken_value))
    print("abs of difference: " + str(abs(wolfram_value - eitken_value)))
    print("---")


# генерируем точки на верхней дуге единичной окружности и смотрим модуль разности со значением первых 10 ** 6 членов
# точки на окружности, потому что внутри окружности сходимость быстрее
# можно видеть, что в точке (1; 0) она расходится и график этому соответсвтует
def draw_speed():
    step = 0.01
    x = -1
    y = 0j
    n = 10 ** 3
    data_x = []
    data_y = []
    while x <= 1:
        accurate_value = s(x + y)
        eitken = s_eitken(x + y, n)
        data_x.append(x)
        data_y.append(np.log10(1 / abs(accurate_value - eitken)))
        x += step
        y = np.sqrt(1 - x ** 2) * 1j
    plt.subplot(211)
    plt.title("speed conversion")
    plt.plot(data_x, data_y)
    plt.ylabel("log10(1 / |accurate - eitken|)")
    plt.xlabel("z")


def main():
    plt.figure(1)
    calculate_value(-0.9, -0.720117)
    calculate_value(-1, -0.7853981633974483)
    calculate_value(np.e ** (3j * np.pi / 4), -0.647215 + 0.486294j)
    calculate_value(1j, -0.243747747 + 0.86697299j)
    draw_speed()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
