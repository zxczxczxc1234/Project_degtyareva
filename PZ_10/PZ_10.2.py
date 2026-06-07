#Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое, количество пробельных символов. 
# Сформировать новый файл, 
# в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.
f = open('PZ_10/стих.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

print("содержимое исходного файла")
print(''.join(lines))

full_text = ''.join(lines)
print("кол-во пробельных символов:", full_text.count(' '))

f_out = open('PZ_10/новый_стих.txt', 'w', encoding='utf-8')

for i in range(len(lines)):
    if i == 2:
        coded_line = ""
        for char in lines[i]:
            coded_line = coded_line + str(ord(char)) + " "
        f_out.write(coded_line + '\n')
    else:
        f_out.write(lines[i])

f_out.close()