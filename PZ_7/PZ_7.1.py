#Дана строка. подсчитать количество содержащихся в ней прописных латинских букв
text = input("Введите строку: ")

uppercase_letters = []

for char in text:
    if 'a' <= char <= 'z':
        uppercase_letters.append(char)

count = len(uppercase_letters)
print(f"Количество прописных латинских букв: {count}")
