# Семинар 1 Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day = ['Понедельник', 'Вторник', 'Среда',
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
for index, value in enumerate(day, 1):
    print(index, value)

num = int(input("Введите номер деня недели: "))

d = ''.join(list(filter(lambda x: x == day[num - 1], day)))

if num < 6 and num > 0:
    print(f"{d} Нет")
elif num > 5 and num < 8:
    print(f"{d} Да")
else:
    print("Ошибка ввода")