import math
# число друзей
num_friends = [100,49,41,40,25,21,21,19,19,18,
               18,16,15,15,15,15,14,14,13,13,
               13,13,12,12,11,10,10,10,10,10,
               10,10,10,10,10,10,10,10,10,10,
               9,9,9,9,9,9,9,9,9,9,
               9,9,9,9,9,9,9,9,8,8,
               8,8,8,8,8,8,8,8,8,8,
               8,7,7,7,7,7,7,7,7,7,
               7,7,7,7,7,7,6,6,6,6,
               6,6,6,6,6,6,6,6,6,6,
               6,6,6,6,6,6,6,6,5,5,
               5,5,5,5,5,5,5,5,5,5,
               5,5,5,5,5,4,4,4,4,4,
               4,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,3,3,3,3,3,
               3,3,3,3,3,3,3,3,3,3,
               3,3,3,3,3,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,
               1,1,1,1]
v = [5, 6, 7]

# размах 
def data_range(x):
    return max(x) - min(x)

# центр распределения(среднее значение)
def mean(x):
    return sum(x) / len(x)

# вектор отклонений от среднего (центрированный вектор)
def de_mean(x):
    """пересчитать х, вычтя его среднее (среднее результата будет = 0)"""
    x_bar = mean(x) # среднее
    return [x_i - x_bar for x_i in x]

# скалярное произведение векторов это сумма их покомпонентых произведений
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# сумма квадратов
def sum_of_squares(v):
    return dot(v, v)

# дисперсия это средняя сумма квадратов отклонений от среднего
def variance(x):
    '''предпологается, что вектор x состоит минимум из двух компонентов'''
    n = len(x)
    devitations = de_mean(x)
    return sum_of_squares(devitations) / (n - 1)

# стандартное отклонение, то есть корень от дисперсии
def standart_devitation(x):
    return math.sqrt(variance(x))

# нахождение квантиля значение ниже которого расположен определенный процент данных
def quantile(x, p):
    # вернет значение в х соответствующему проценту p данных
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# интерквартильный размах менее чувствителен к выбросам чем стандартное отклонение
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)