A = [[1, 2, 3], 
     [4, 5, 6]]

def shape_A(A):
    num_rows = len(A)   # количество строк, то есть количество списков в списке
    num_cols = len(A[0]) if A else 0 # колво столбцов - колво элементов в первом списке
    return num_rows, num_cols

# получить i-ю строку
def get_row(A, i):
    return A[i] # A[i] - это i-я строка

# получить i-ю строку
def get_col(A, j):
    return [A_i[j] # j-й элемент строки A_i
            for A_i in A]  # для каждой строки A_i

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) 
             for j in range(num_cols)] # [entry_fn(i,O), ... ] сгенерируются элементы для первого списка при помощи входной ф-ии
             for i in range(num_rows)] # а затем создатся второй список 

def is_diagonal(i, j):
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # пользователь 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # пользователь 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # пользователь 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # пользователь 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # пользователь 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # пользователь 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # пользователь 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # пользователь 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # пользователь 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # пользователь 9

friend_of_five = [i for i, is_friend in enumerate(friendships[5]) if is_friend]

print(friend_of_five)
