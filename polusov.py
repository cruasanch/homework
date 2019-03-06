"""Полусовершенные числа до заданного"""
lenght = int(input('Введите предел для полусовершенных чисел - '))
print("Все полусовершенные числа до", lenght, ":")
def func(i):
    k = 0
    for j in range(1, i):
        if i % j == 0:
            k += j
    return k
for i in range(1,lenght+1):
    if i <= func(i):
        print(i)
