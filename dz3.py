# Семинар 5 Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

file = open('source_text.txt', 'r')
text = "".join(i for i in file)
text = list(text)
text.append(" ")
file.close()
print(f"Текст из файла: {''.join(text)}")

compression = []
letters = []
numbers = []
recovery = []

summa = 0
sumbol = text[0]

for i in text:
    if i == sumbol:
        summa += 1
    else:
        compression.append(summa)
        compression.append(sumbol)
        numbers.append(summa)
        letters.append(sumbol)
        sumbol = i
        summa = 1
        
def CompressionFile():
    compression_file = list(str(i) for i in compression)
    compression_file = ''.join(compression_file)
    file = open('RLE.txt', 'w')
    file.write(str(compression_file))
    file.close()
    print(f"Сжатый текст: {compression_file}")
    
def Recovery():
    recovery = list(
        map(lambda i: letters[i] * numbers[i], range(len(letters))))
    recovery = ''.join(recovery)
    file = open('recovery.txt', 'w')
    file.write(str(recovery))
    file.close()
    print(f"Востановленный текст: {recovery}")

CompressionFile()
Recovery()