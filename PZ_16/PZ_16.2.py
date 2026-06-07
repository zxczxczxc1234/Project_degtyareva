#создайте базовый класс "форма" со свойствами "цвет" и "тип". 
# от этого класса унаследуйте класс "круг" и добавьте в него свойство "радиус". определите методы вычисления площади и периметра."
class Shape:

    def __init__(self, color: str, shape_type: str):
        self.color = color
        self.shape_type = shape_type


class Circle(Shape):

    def __init__(self, color: str, radius: float):
        super().__init__(color, shape_type="Круг")
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self) -> float:
        return 2 * 3.14 * self.radius


circle1 = Circle(color="Красный", radius=5)
circle2 = Circle(color="Синий", radius=10)
circle3 = Circle(color="Зеленый", radius=2.5)

print("информация о 3 кругах")

print(f"Форма: {circle1.shape_type}, Цвет: {circle1.color}, Радиус: {circle1.radius}")
print(f"Площадь: {circle1.calculate_area():.2f}, Периметр: {circle1.calculate_perimeter():.2f}" and "\n")
print(f"Форма: {circle2.shape_type}, Цвет: {circle2.color}, Радиус: {circle2.radius}")
print(f"Площадь: {circle2.calculate_area():.2f}, Периметр: {circle2.calculate_perimeter():.2f}" and "\n")
print(f"Форма: {circle3.shape_type}, Цвет: {circle3.color}, Радиус: {circle3.radius}")
print(f"Площадь: {circle3.calculate_area():.2f}, Периметр: {circle3.calculate_perimeter():.2f}")


