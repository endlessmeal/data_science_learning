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

# центр распределения(среднее значение)
def mean(x):
    return sum(x) / len(x)

def median(v):
    
    n = len(v)
    sorted_v = sorted(v)
    mid = n // 2

    if n % 2 == 0:
        return sorted_v[mid]
    else:
        lo = mid - 1
        hi = mid
        return (sorted_v[lo] + sorted_v[hi]) / 2

# нахождение квантиля значение ниже которого расположен определенный процент данных
def quantile(x, p):
    # вернет значение в х соответствующему проценту p данных
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_counts = max(counts.values())
    print(max_counts)
    print(counts.items())
    return [x_i for x_i, count in counts.items() if count == max_counts]

print(mode(num_friends))
