from matplotlib import pyplot as plt 

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title('Номинальный ВВП')

plt.ylabel('Млрд. долларов')
plt.show()

