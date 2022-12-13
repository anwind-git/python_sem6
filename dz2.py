# Семинар 2 Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите число: '))
number = str(number)
number = list(filter(lambda x: x != ".", number))
number = list(int(i) for i in number)

print(f'Сумма чисел равна {sum(number)}')
