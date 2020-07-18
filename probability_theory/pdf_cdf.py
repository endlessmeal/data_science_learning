import math
import matplotlib.pyplot as plt
# ДФР для РАВНОМЕРНОГО распределения (или функция плотности)
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# ИФР для РАВНОМЕРНОГО распределения
def uniform_cdf(x):
    """возвращает вероятность того, что равномерно распределенная случайнаявеличина <=х"""
    if x < 0:   return 0 # величина не может быть меньше 0
    elif x < 1: return x # например P(x <= 0.4) = 0.4
    else:       return 1 # величина всегда меньше 1

#ДФР для нормального распределения, дефолтные мю и сигма в случае стандартного нормального распределения
def normal_pdf(x, mu = 0, sigma = 1):
    return math.exp((-(x - mu) ** 2) / (2 * sigma ** 2)) / math.sqrt(2 * math.pi) * sigma

xs = [x / 10 for x in range(-50, 50)]

# несколько графиков для дфр норм распр
def some_graphs_with_normal_pdf():
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='мю = 0, сигма=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='мю = 0, сигма=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='мю = 0, сигма=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='мю = -1, сигма=1')
    plt.legend()
    plt.title('Несколько ДФР нормального распределения')

# ИФР для нормального распределения, то есть получаем вероятность при случайной величине x
def normal_cdf(x, mu=0, sigma=1):
    '''erf это функция для интеграла вероятности'''
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# несколько графиков для ифр норм распр
def some_graphs_with_normal_cdf():
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='мю = 0, сигма=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='мю = 0, сигма=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='мю = 0, сигма=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='мю = -1, сигма=1')
    plt.ylabel('Вероятность')
    plt.xlabel('Случайные величины')
    plt.legend(loc=4) # справа внизу
    plt.title('Несколько ИФР нормального распределения')

# получаем максимально приближенную случайную величину к вероятности p с помощью двоичного поиска
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1

    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    
    return mid_z


# some_graphs_with_normal_cdf()
plt.show()