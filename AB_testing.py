import math
from example_coin_flip import two_sided_p_value
# оценочные параметры, где N количество показов, а n количество кликов
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

# статистика A/B тестирования
def a_b_testing(N_a, n_a, N_b, n_b):
    p_A, sigma_A = estimated_parameters(N_a, n_a)
    p_B, sigma_B = estimated_parameters(N_b, n_b)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

# статистика
z = a_b_testing(1000, 200, 1000, 180) # -1.14

# вероятность наблюдать такую большую разницу будет
two = two_sided_p_value(z) # 0.254

