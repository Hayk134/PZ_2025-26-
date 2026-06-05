'''
30. Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат" переопределите методы,
 связанные с вычислением площади и периметра.
'''
class Shape:
    width = 0
    height = 0


class Rectangle(Shape):

    def area(self):
        return self.width * self.height


class Square(Shape):

    def area(self):
        return self.width * self.width

    def perimeter(self):
        return self.width * 4

r = Rectangle()
r.width = 4
r.height = 5
print(r.area())

s = Square()
s.width = 4
print(s.area(), s.perimeter())