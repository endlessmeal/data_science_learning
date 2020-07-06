import matplotlib.pyplot as plt
from collections import Counter

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

friends_counts = Counter(num_friends)
xs = range(101) # макс значение
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Гистограмма количества друзей')
plt.ylabel('Количество человек')
plt.xlabel('Количество друзей')
plt.show()

num_points = len(num_friends) # число точек данных
largest_value = max(num_friends) # наибольшее колво друзей 100
smallest_value = min(num_friends) # наименьшее колво друзей 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

# центр распределения(среднее значение)
def mean(x):
    return sum(x) / len(x)

print(mean(num_friends))
print(num_points)

