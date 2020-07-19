import math
from probability_theory.pdf_cdf import normal_cdf, inverse_normal_cdf
import random
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


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5) # 500, 15.81

# стандартное отклонение и мат ожидание при вероятности 0.55(то есть в сторону орла)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55) # 550, 15.7

# 95 % границы при условии, что p = 0.5
lo, hi = normal_two_sided_bound(0.95, mu_0, sigma_1) # 469, 530

# ошибка второго рода означает: не удалось отклонить нулевую гипотезу; 
# это происходит, когда X все еще внутри первоначального интервала
type_2_probability = normal_probability_beetwen(lo, hi, mu_1, sigma_1) # 0.11
# мощность
power = 1 - type_2_probability # 0.887


#####
#
# p-значения
#
######

# двустороннее p значение
def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # если x больше среднего значения, то значения в хвосте больше x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # если x меньше среднего значения, то значения в хвосте меньше x
        return 2 * normal_probability_below(x, mu, sigma)

# 529.5 так при таком значении намного точнее вероятность получится при том, что выпадет как минимум 530 орлов
two_sided_p_value(529.5, mu_0, sigma_0) # 0.62

# проверка p значения
def check_two_sided_p_value():
    extreme_value_count = 0 # количество предельных значений
    for _ in range(100000):
        num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
        if num_heads >= 530 or num_heads <= 470:
            extreme_value_count += 1
    return extreme_value_count / 100000

# check_two_sided_p_value() # 0.62

#####
#
# доверительные интервалы
#
######

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

# в этом случае вывод, что монет неуравновешена - не делается, так как значения лежат в пределах доверительного интервала
normal_two_sided_bound(0.95, mu, sigma) # 0.490, 0.555

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

normal_two_sided_bound(0.95, mu, sigma) # 0.490, 0.555
