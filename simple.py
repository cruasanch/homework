"""Простые числа до заданного числа"""
lenght = int(input('Введите предел для простых чисел - '))
simple=[]
for i in range(2, lenght+1):
    for j in simple:
        if i % j == 0:
            break
    else:
        simple.append(i)
print(simple)