"""Задача такая: функция которая высчитывает шаги для каждого числа до лимита ,
 заданного юзером, и возвращает число, у которого максимальное количество шагов, и само количество шагов"""
def kollatz(n):
    ch = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        ch += 1
    return ch
ch1 = []
leng = int(input('Введите предел для проверки - '))
for i in range(1, leng + 1):
    ch1.append(kollatz(i))
from functools import reduce
maxs = reduce(lambda a, b: a if (a > b) else b, ch1)
maxv = ch1.index(reduce(lambda a, b: a if (a > b) else b, ch1))
print('У числа', maxv + 1, 'максимальное кол-во шагов -', maxs)
