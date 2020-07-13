from matplotlib import pyplot as plt 

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67] # друзья 
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190] # минуты. 
labels = ['а', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] # метки

plt.scatter(friends, minutes) # отобразит все точки у которых по иксам friend, а по игрекам minutes

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, # подпись для каждой точки
                xy = (friend_count, minute_count), # координаты для каждой точки
                xytext = (5, -5), # позиция подписи для точки относительно точки
                textcoords='offset points')


plt.title("Зависимость между количеством минут и числом друзей") 
plt.xlabel("Число друзей")
plt.ylabel("Время, проводимое на сайте ежедневно, мин") 
plt.show()