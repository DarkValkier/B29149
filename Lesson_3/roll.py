import random

for i in range(10):
    if random.randint(1, 100) <= 30:
        print('Прокнуло')
    else:
        print('Не прокнуло')