import matplotlib.pyplot as plt
from functools import partial

# отношение приращений
def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x ** 2

def derivative(x):
    return 2 * x

# оценка производной
derivative_estimate = partial(difference_quotient, square, h=0.00001)

# xs = range(-10,10)
# plt.title('Фактические производные и их оценки в сравнении')
# plt.plot(xs, [derivative(x) for x in xs], 'rx', label='Факт')
# plt.plot(xs, [derivative_estimate(x) for x in xs], 'b+', label='Оценка')
# plt.legend(loc=9)
# plt.show()

import random
from linear_algebra.vectors import distance
def step(v, direction, step_size):
    return [v_i + step_size * direction_i 
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

v = [random.randint(-10,10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        print(v, next_v)
        break
    v = next_v


