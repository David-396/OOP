from Shapes import Shape
from Square import Square

class Rectangle(Shape):
    def __init__(self, height, length):
        try:
            float(height), float(length)
        except Exception:
            raise ValueError("you can enter only numbers!")

        super().__init__()
        self.height = height
        self.length = length


    def get_area(self):
        return self.height*self.length
    def get_perimeter(self):
        return self.length*2 + self.height*2

    def __repr__(self):
        return f"Rectangle(height = {self.height}, length = {self.length})"

    @staticmethod
    def operators_check_and_raise(other, operator):
        if not isinstance(other, (Square, Rectangle)):
            raise TypeError(f"operator {operator} is only between Rectangle and Rectangle or Square")

    # >=
    def __ge__(self, other):
        Rectangle.operators_check_and_raise(other, '>=')
        return self.get_area() >= other.get_area()
    # >
    def __gt__(self, other):
        Rectangle.operators_check_and_raise(other, '>')
        return self.get_area() > other.get_area()
    # <
    def __lt__(self, other):
        Rectangle.operators_check_and_raise(other, '<')
        return self.get_area() < other.get_area()
    # <=
    def __le__(self, other):
        Rectangle.operators_check_and_raise(other, '<=')
        return self.get_area() <= other.get_area()
    # ==
    def __eq__(self, other):
        Rectangle.operators_check_and_raise(other, '==')
        return self.get_area() == other.get_area()
    # !=
    def __ne__(self, other):
        Rectangle.operators_check_and_raise(other, '!=')
        return self.get_area() != other.get_area()

    @staticmethod
    def calc_check_and_raise(other, operator):
        if not isinstance(other, Rectangle):
            raise TypeError(f"operator {operator} is only between Rectangle and Rectangle")

    # +
    def __add__(self, other):
        Rectangle.calc_check_and_raise(other, '+')
        return Rectangle(self.height + other.height, self.length + other.length)
    # +=
    def __iadd__(self, other):
        Rectangle.calc_check_and_raise(other, '+=')
        return Rectangle(self.height + other.height, self.length + other.length)
    # -
    def __sub__(self, other):
        Rectangle.calc_check_and_raise(other, '-')
        new_rec =  Rectangle(self.height - other.height, self.length - other.length)
        if new_rec.length < 0 or new_rec.height < 0:
            return Rectangle(0,0)
        return new_rec
    # -=
    def __isub__(self, other):
        Rectangle.calc_check_and_raise(other, '-=')
        new_rec =  Rectangle(self.height - other.height, self.length - other.length)
        if new_rec.length < 0 or new_rec.height < 0:
            return Rectangle(0,0)
        return new_rec