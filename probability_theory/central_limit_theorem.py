import random
from collections import Counter
import matplotlib.pyplot as plt
import math

# независимое испытание Бернулли 
# в котором имеется всего два исхода (1 или 0)
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# биномиальное распределение
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# ИФР для нормального распределения, то есть получаем вероятность при случайной величине x
def normal_cdf(x, mu=0, sigma=1):
    '''erf это функция для интеграла вероятности'''
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# num_points это число повторов, а n это случайные величины
def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    histogram = Counter(data)
    print(histogram)
    # столбачатая диаграмма, показывающая фактические биномиальные выборки
    plt.bar([x for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu = p * n # мат ожидание
    sigma = math.sqrt(n * p * (1 - p)) # стандартное отклонение

    # линейный график, показывающий нормальное приближение   
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]

    plt.plot(xs, ys)
    plt.title('Биномиальное распределение и его нормальное приближение')
    plt.show()


def make_hist_binom(p, n, trials):
    data = [binomial(n, p) for _ in range(trials)]
    
    dots = Counter(data)
    print(dots)
    plt.scatter([x for x in dots.keys()], [v / trials for v in dots.values()])
    plt.xlabel('Количество раз выпаданий решки')
    plt.ylabel('Вероятность, что решка выпадет столько раз')
    plt.show()

print(binomial(1000, 0.5))
# print([binomial(100, 0.5) for _ in range(10)])
# make_hist(0.75, 100, 10000)
# make_hist_binom(0.5, 100, 1000)


