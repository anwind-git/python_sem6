# Дан список, вывести отдельно буквы и цифры. a = ( "a", 'b', '2', '3' ,'c')

# line = input("Введите строку: ")

line = ("a", 'b', '2', '3', 'c')

digits = ''.join([i for i in line if i in '0123456789'])
letters = ''.join([j for j in line if j not in digits])

print(list(digits))
print(list(letters))