#Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
#одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).
def shift_right(arr):
    if len(arr) <= 1:
        return arr
    last_element = arr.pop()
    arr.insert(0, last_element)
    return arr
  
N = int(input("Введите размер списка N: "))
numbers = list(map(int, input(f"Введите {N} чисел через пробел: ").split()))

result = shift_right(numbers.copy())
print("Результат:", result)