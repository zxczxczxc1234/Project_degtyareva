import random

get_column = lambda matrix, idx: list(map(lambda row: row[idx], matrix))
get_sum = lambda data_list: sum(data_list)
get_min = lambda data_list: min(data_list)

format_matrix = lambda matrix: "\n".join(map(str, matrix))

matrix = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

print("исходная матрица:")
print(format_matrix(matrix))


#1. Для каждого столбца матрицы с четным номером найти сумму ее элементов.
print("\n задание 1")
column_2 = get_column(matrix, 1)
sum_2 = get_sum(column_2)
print(f"второй столбец: {column_2} | сумма элементов = {sum_2}")


#2. В матрице найти минимальный элемент в предпоследнем столбце
print("\n задание 2")
penultimate_column = get_column(matrix, 1) 
min_element = get_min(penultimate_column)

print(f"предпоследний столбец: {penultimate_column}")
print(f"минимальный элемент в нем: {min_element}")