# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

print('Введите размер массива:')
N = int(input())
list = [random.randint(-100, 100) for i in range(N)]


def Afterminuszero(list):
    result = []
    for element in list:
        result.append(element)
        if element < 0:
            result.append(0)
    return result


trans = Afterminuszero(list)
print(f'Массив {list}')
print(f'Измененный массив{trans}')
