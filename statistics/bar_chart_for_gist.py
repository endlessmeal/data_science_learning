from collections import Counter
from matplotlib import pyplot as plt 

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

decile = lambda grade: grade // 10 * 10 # дециль - десятая часть от числа
histogram = Counter(decile(grade) for grade in grades) # закидываем в лист десятые части чисел без повторений с помощью Counter

plt.bar(histogram.keys(), # для столбцов
        histogram.values(), # для высоты столбцов
        8)                  # для ширины столбцов

plt.axis([-5, 105, 0, 5]) # -5 and 105 are x axis coordinates, 0 and 5 are for y

plt.xticks([10 * i for i in range(11)]) # метки по оси Х

plt.show()