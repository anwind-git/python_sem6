# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел

number = input('Вводите числа через пробел: ')

number = number.split()

def select(f, col):
    return [f(x) for x in col]

number = select(int, number)

def FilterNumber(in_num):
    return in_num >= 10 and in_num < 100 or in_num <= -10 and in_num > -100

result = filter(FilterNumber, number)
result = " ".join(select(str, result))

print(f"Отфильтрованный список: {result}")