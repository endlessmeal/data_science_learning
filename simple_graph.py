from matplotlib import pyplot as plt 

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title('Номинальный ВВП')

plt.ylabel('Млрд. долларов')
plt.show()


# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] # 
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] # ВВП
# # создать линейную диаграмму: годы по оси X, ВВП по оси Y
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# # добавить название диаграммы
# plt.title("Номинальный ВВП")
# # добавить подпись к оси Y
# plt.ylabel('млрд')
# plt.show()