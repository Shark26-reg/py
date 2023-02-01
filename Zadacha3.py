"""Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369"""

n = int(input("Введите целое положительное число: "))
tmp = str(n)
t1 = tmp + tmp
t2 = tmp + tmp + tmp
result = n + int(t1) + int(t2)
print(f"n + nn + nnn = {result}")