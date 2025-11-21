#Описать функцию ShiftLeft3, выполняющий левый циклический сдвиг. A,B,C явл входными и выходными
#С помощью этой функции выполнить левый циклический сдвиг для двух данных наборов из трех чисел A1B1C1,A2B2C2
def ShiftLeft3(A, B, C):
    return B, C, A

A1 = float(input("Введите A1: "))
B1 = float(input("Введите B1: "))
C1 = float(input("Введите C1: "))

print(f"Исходник: {A1}, {B1}, {C1}")

A1, B1, C1 = ShiftLeft3(A1, B1, C1)
print(f"После сдвига: {A1}, {B1}, {C1}")

A2 = float(input("Введите A2: "))
B2 = float(input("Введите B2: "))
C2 = float(input("Введите C2: "))

print(f"Исходник: {A2}, {B2}, {C2}")

A2, B2, C2 = ShiftLeft3(A2, B2, C2)
print(f"После сдвига: {A2}, {B2}, {C2}")