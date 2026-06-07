#1.Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать последовательность, содержащую
# положительные числа и отрицательные числа. Найти
# количество элементов в полученных последовательностях.
import random

get_len = lambda data_list: len(data_list)

N = int(input("введите количество чисел: "))

source_list = [random.randint(-5, 5) for _ in range(N)]

positive_list = [x for x in source_list if x > 0]
negative_list = [x for x in source_list if x < 0]

print(f"исходная последовательность: {' '.join(map(str, source_list))}")

print(f"положительные числа: {' '.join(map(str, positive_list))} , количество: {get_len(positive_list)}")
print(f"отрицательные числа: {' '.join(map(str, negative_list))} , количество: {get_len(negative_list)}")