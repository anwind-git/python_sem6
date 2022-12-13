# Преобразовать набора списков

user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

x1, x2, x3 = map(list, zip(user, ids, salary))
data = list(zip(user, ids, salary))

print("Преобразование набора списков:")
print(x1, x2, x3, sep="\n")

x1, x2, x3 = zip(*data)
print("Возврат в исходное стостояние:")
print(list(x1), list(x2), list(x3), sep="\n")
