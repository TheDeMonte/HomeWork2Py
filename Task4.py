import datetime


def random_number(min, max):
    now = str(datetime.datetime.now())
    rnd = float(now[::-1][:3:])/1000
    return int(min + rnd*(max-min))


n = random_number(1, 1000)
k = random_number(1, 500)
b = []
for i in range(n):
    b.append(random_number(0, 2 * 10 ^ 9))
f = b[k]
print('Количество элементов =', n, 'Необходимо выбрать', k, 'элемент.')
print('Выбранный элемент -', f)
