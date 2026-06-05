#Организовать и вывести последовательность из N случайных целых чисел. 
# Из исходной последовательности организовать последовательность, содержащую положительные числа и последовательность, содержащую отрицательные числа. 
# Найти количество элементов в полученных последовательностях.
def get_max_value(data):
    numeric_data = [int(x) for x in data if x and x.isdigit()]
    return max(numeric_data) if numeric_data else None

def process_file_part1(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            numeric_values = [int(x) for x in parts if x.isdigit()]

            if numeric_values:
                max_in_line = max(numeric_values)
                outfile.write(f"{line.strip()} {max_in_line}\n")

# Пример использования:
input_file_1 = 'input.txt'  # Укажите имя вашего входного файла
output_file_1 = 'output_part1.txt' # Выходной файл для первой части

process_file_part1(input_file_1, output_file_1)