from matplotlib import pyplot as plt 

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256] # дисперсия 
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1] # квадрат смещения

total_error = [x + y for x, y in zip(variance, bias_squared)] # складывам числа в полученных кортежах, которые сделал zip и кладем их в лист

xs = [i for i, _ in enumerate(variance)] # enumerate вернет лист ТОЛЬКО с индексами так как цикл без учета второй переменной

plt.plot(xs, variance, 'g-', label='Дисперсия') # зеленая сплошная линия

plt.plot(xs, bias_squared, 'r-.', label='смещение^2') # красная штрихпунктирная

plt.plot(xs, total_error, 'b:', label='суммарная ошибка') # синяя пунктирная

plt.legend(loc=9) # легенда будет отображена сверху посередине
plt.xlabel("Сложность модели")
plt.title("Компромисс между смещением и дисперсией") 
plt.show()