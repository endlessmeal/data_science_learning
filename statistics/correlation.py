import indicators_of_variations as iv
import datasets
import matplotlib.pyplot as plt

# отклонение от среднего для двух датасетов
def covariance(x, y):
    n = len(x) # за длину берем первый набор данных данных так как их количество совпадает
    return iv.dot(iv.de_mean(x), iv.de_mean(y)) / (n - 1) # возвращаем среднее от скаляряного произведения двух центрированных векторов

# корреляция - в ней ковариация распределяется между стандартными отклонениями между двумя переменными
def correlation(x, y):
    stdev_x = iv.standart_devitation(x) # используем стандартное отклонение так как хотим уйти от входных величин
    stdev_y = iv.standart_devitation(y) # стандартное отклонение это корень от дисперсии

    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # если переменные не меняются, то корреляция равна нулю

print(correlation(datasets.num_friends, datasets.daily_minutes)) # корреляция с выбросом будет равна 0.24

outlier = datasets.num_friends.index(100) # выброс данных на 100 позиции(там пользователь со 100 друзьями проводит время в соц сети 1 минуту)

num_friends_good = [x 
                    for i, x in enumerate(datasets.num_friends) 
                    if i != outlier]
daily_minutes_good = [x 
                      for i, x in enumerate(datasets.daily_minutes) 
                      if i != outlier]

plt.scatter(num_friends_good, daily_minutes_good)
plt.ylabel('Количество минут в день')
plt.xlabel('Количество друзей')
plt.show()

print(correlation(num_friends_good, daily_minutes_good)) # корреляция за исключением выброса будет близка к идеальной корреляции 0.57