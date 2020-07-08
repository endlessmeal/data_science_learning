import random

def random_kid():
    return random.choice(['boy', 'girl'])

both_girl = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(100000): # генерируем 100к семей

    younger = random_kid()
    older = random_kid()

    if older is 'girl': # девочка старшая?
        older_girl += 1
    if older is 'girl' and younger is 'girl': # обе?
        both_girl += 1
    if older is 'girl' or younger is 'girl': # любая из двух?
        either_girl += 1
    
print(f'P(обе | старшая): {both_girl / older_girl}') # 0.5 то есть 1/2
print(f'P(обе | любая): {both_girl / either_girl}') # 0.3 то есть 1/3