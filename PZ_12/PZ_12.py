import random

get_column = lambda matrix, idx: list(map(lambda row: row[idx], matrix))
sum_column = lambda column: sum(column)
get_penultimate = lambda matrix: list(map(lambda row: row[-2], matrix))
min_value = lambda column: min(column)
print_matrix = lambda matrix: print("\n".join(str(row) for row in matrix))

matrix = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

print("исходная матрица")
print_matrix(matrix)

print("\n задание 1")
column_elements = get_column(matrix, 1)
column_sum = sum_column(column_elements)
print(f"второй столбец (индекс 1): {column_elements} | Сумма = {column_sum}")

print("\n задание 2")
penultimate_column = get_penultimate(matrix)
min_value_result = min_value(penultimate_column)
print(f"предпоследний столбец: {penultimate_column}")
print(f"минимальный элемент в нем: {min_value_result}")