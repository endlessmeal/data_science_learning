import math
from probability_theory.pdf_cdf import normal_cdf, inverse_normal_cdf

# аппроксимация биномальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n, p):
    '''находим мю и сигма соответсвующие биномиальному распределению'''
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#####
#
# вероятности, что нормальная случайная величина лежит в интервале
#
######

# вероятность, что нормальная случайная величина лежит ниже порогового значения
normal_probability_below = normal_cdf

# вероятность, что норм случ величина лежит над пороговым значением
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# между
def normal_probability_beetwen(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# за пределами
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_beetwen(lo, hi, mu, sigma)

#####
#
# границы для нормальной случайной величины 
#
######

# верхняя граница нормальной величины
def normal_upper_bound(probability, mu=0, sigma=1):
    # возвращает z для которого P(Z <= z) = probability
    return inverse_normal_cdf(probability, mu, sigma)

# нижняя граница нормальной величины
def normal_lower_bound(probability, mu=0, sigma=1):
    # возвращает z для которого P(Z >= z) = probability
    return inverse_normal_cdf(1 - probability, mu, sigma)

# двусторонная граница норм величины
def normal_two_sided_bound(probability, mu=0, sigma=1):
    # возвращает симметричные границы вокруг среднего значения, в пределах которого расположена вероятность
    tail_probability = (1 - probability) / 2

    # верхняя граница должна иметь значение хвостовой вероятности выше ее(то есть все Z расположены выше)
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # нижняя граница должна иметь значение хвостовой вероятности ниже ее (то есть все Z расположены ниже)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print(mu_0, sigma_0) 

# 95 % границы при условии, что p = 0.5
lo, hi = normal_two_sided_bound(0.95, mu_1, sigma_1)
print(lo, hi)

# стандартное отклонение и мат ожидание при вероятности 0.55(то есть в сторону орла)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
print(mu_1, sigma_1)

type_1_probability = normal_probability_beetwen(lo, hi, mu_0, sigma_0)
print(type_1_probability)

type_2_probability = normal_probability_beetwen(lo, hi, mu_1, sigma_1)
print(type_2_probability)
