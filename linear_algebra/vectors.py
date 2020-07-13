from functools import reduce
import math

# сложение двух векторов
def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

# вычитание двух векторов
def vector_substract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

# покомпонентное сложение списка векторов
def vector_sum(vectors):
    return reduce(vector_add, vectors)

# умножение вектора на скаляр, где c - это число, v - вектор
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

"""вычислить вектор, чей i-й элемент - это среднее значение
всех i-х элементов входящих векторов"""
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# скалярное произведение векторов это сумма их покомпонентых произведений
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# сумма квадратов
def sum_of_squares(v):
    return dot(v, v)

# величина(длина) вектора
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# расстояние между двумя векторами
def distance(v, w):
    return magnitude(vector_substract(v, w))