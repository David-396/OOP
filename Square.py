from Shapes import Shape
from Rectangle import Rectangle

class Square(Shape):
    def __init__(self, side):
        try:
            float(side)
        except Exception:
            raise ValueError("you can enter only numbers!")

        super().__init__()
        self.side =side

    def get_area(self):
        return self.side**2
    def get_perimeter(self):
        return self.side * 4

    def __repr__(self):
        return f"Square(side = {self.side})"

    @staticmethod
    def operators_check_and_raise(other, operator):
        if not isinstance(other, (Square, Rectangle)):
            raise TypeError(f"operator {operator} is only between Square and Square or Rectangle")

    # >=
    def __ge__(self, other):
        Square.operators_check_and_raise(other, '>=')
        return self.get_area() >= other.get_area()
    # >
    def __gt__(self, other):
        Square.operators_check_and_raise(other, '>')
        return self.get_area() > other.get_area()
    # <
    def __lt__(self, other):
        Square.operators_check_and_raise(other, '<')
        return self.get_area() < other.get_area()
    # <=
    def __le__(self, other):
        Square.operators_check_and_raise(other, '<=')
        return self.get_area() <= other.get_area()
    # ==
    def __eq__(self, other):
        Square.operators_check_and_raise(other, '==')
        return self.get_area() == other.get_area()
    # !=
    def __ne__(self, other):
        Square.operators_check_and_raise(other, '!=')
        return self.get_area() != other.get_area()

    @staticmethod
    def calc_check_and_raise(other, operator):
        if not isinstance(other, Square):
            raise TypeError(f"operator {operator} is only between Square and Square")

    # +
    def __add__(self, other):
        Square.calc_check_and_raise(other, '+')
        return Square(self.side + other.side)