# Даны три числа
#найти среднее из них(то число, расположенное между наибольшим и наименьшим)
try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))
    if (b < a < c) or (c < a < b):
        middle = a
    elif (a < b < c) or (c < b < a):
        middle = b
    else:
        middle = c
    print(f"Среднее число: {middle}")
except ValueError:
    print("Неверный ввод.Попробуйте снова.")
