#2. Составить генератор (yield), который выводит из строки только цифры
def digit_generator(input_string):
    for char in input_string:
        if char.isdigit():
            yield char

source_string = "в 2026 году мне исполнилось 18 лет"
print(f"исходная строка: '{source_string}'")

result_digits = list(digit_generator(source_string))

print(f"найденные цифры: {' '.join(digit_generator(source_string))}")

