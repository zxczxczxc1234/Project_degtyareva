#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого минимального элемента:
# Умножаем все элементы на минимальный элемент:
numbers = [15, -7, 23, -14, 8]

f = open('isxod_chisla.txt', 'w', encoding='utf-8')
for num in numbers:
    f.write(str(num) + ' ')
f.close()

f = open('isxod_chisla.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

nums = []
for s in text.split():
    nums.append(int(s))

min_num = min(nums)
min_idx = nums.index(min_num)

result = []
for x in nums:
    result.append(x * min_num)

f = open('resultat.txt', 'w', encoding='utf-8')
f.write('исходные данные: ' + str(nums) + '\n')
f.write('количество элементов: ' + str(len(nums)) + '\n')
f.write('индекс первого минимального элемента: ' + str(min_idx) + '\n')
f.write('умножение элементов на минимальный элемент: ' + str(result) + '\n')
f.close()