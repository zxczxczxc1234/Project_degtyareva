#Cоздайте класс "машина" с атрибутами "марка", "модель" и "год выпуска". 
# напишите метод, который выводит информацию о машине в формате "марка: марка, модель: модель, год выпуска: год".
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self) -> None:
        print(f"марка: {self.brand}, модель: {self.model}, год выпуска: {self.year}")

car1 = Car(brand="Toyota", model="Camry", year=2021)
car2 = Car(brand="BMW", model="M5", year=2023)
car3 = Car(brand="Lada", model="Vesta", year=2019)

print("Информация о 3 машинах")
car1.display_info()
car2.display_info()
car3.display_info()