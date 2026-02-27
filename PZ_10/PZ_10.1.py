#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого минимального элемента:
# Умножаем все элементы на минимальный элемент:
numbers = [15, -7, 23, -14, 8, -3, 42, -5, 11, -9, 31, -2]

f = open('isxod_chisla.txt', 'w', encoding='utf-8')
for i in range(len(numbers)):
    f.write(str(numbers[i]))
    if i < len(numbers) - 1:
        f.write(' ')
f.close()

f = open('isxod_chisla.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

nums = []
for s in text.split():
    nums.append(int(s))

print('Исходные данные:')
for i in range(len(nums)):
    print(nums[i], end=' ')
print()

min_num = nums[0]
min_idx = 0
for i in range(len(nums)):
    if nums[i] < min_num:
        min_num = nums[i]
        min_idx = i

print('Количество элементов:', len(nums))
print('Минимальный элемент:', min_num)
print('Индекс первого минимального элемента:', min_idx)

result = []
for x in nums:
    result.append(x * min_num)

print('Умножаем все элементы на минимальный элемент:')
for i in range(len(result)):
    print(result[i], end=' ')

f = open('resultat.txt', 'w', encoding='utf-8')
f.write('Исходные данные:\n')
for i in range(len(nums)):
    f.write(str(nums[i]))
    if i < len(nums) - 1:
        f.write(' ')
f.write('\n\n')

f.write('Количество элементов:\n')
f.write(str(len(nums)) + '\n\n')

f.write('Индекс первого минимального элемента:\n')
f.write(str(min_idx) + '\n\n')

f.write('Умножаем все элементы на минимальный элемент:\n')
for i in range(len(result)):
    f.write(str(result[i]))
    if i < len(result) - 1:
        f.write(' ')
f.close()