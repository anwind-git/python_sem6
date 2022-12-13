# Семинар 4 Задача 3: Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import Random, randint

number = int(input("Сколько элементов будет в списке?: "))

def Random(i):
    return randint(1, 20)

def Filter(x):
    num = 0
    for i in list1:
        if i == x:
            num += 1
    if num == 1:
        return x

list1 = [Random(i) for i in range(number)]
list2 = list(filter(Filter, list1))

print(f"Исходный список: {list1}")
print(f"Список неповторяющихся элементов: {list2}")