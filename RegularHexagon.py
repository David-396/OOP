from Shapes import Shape

class RegularHexagon(Shape):
    def __init__(self, side):
        try:
            float(side)
        except Exception:
            raise ValueError("you can enter only numbers!")

        super().__init__()
        self.side = side


    def get_area(self):
        return ((3*(3**0.5)) / 2) * self.side ** 2
    def get_perimeter(self):
        return 6*self.side

    def __repr__(self):
        return f"RegularHexagon(side = {self.side})"

    @staticmethod
    def operators_check_and_raise(other, operator):
        if not isinstance(other, RegularHexagon):
            raise TypeError(f"operator {operator} is only between RegularHexagon and RegularHexagon")

    # >=
    def __ge__(self, other):
        RegularHexagon.operators_check_and_raise(other, '>=')
        return self.get_area() >= other.get_area()
    # >
    def __gt__(self, other):
        RegularHexagon.operators_check_and_raise(other, '>')
        return self.get_area() > other.get_area()
    # <
    def __lt__(self, other):
        RegularHexagon.operators_check_and_raise(other, '<')
        return self.get_area() < other.get_area()
    # <=
    def __le__(self, other):
        RegularHexagon.operators_check_and_raise(other, '<=')
        return self.get_area() <= other.get_area()
    # ==
    def __eq__(self, other):
        RegularHexagon.operators_check_and_raise(other, '==')
        return self.get_area() == other.get_area()
    # !=
    def __ne__(self, other):
        RegularHexagon.operators_check_and_raise(other, '!=')
        return self.get_area() != other.get_area()

    # +
    def __add__(self, other):
        RegularHexagon.operators_check_and_raise(other, '+')
        return RegularHexagon(self.side + other.side)
    # +=
    def __iadd__(self, other):
        RegularHexagon.operators_check_and_raise(other, '+=')
        return RegularHexagon(self.side + other.side)
    # -
    def __sub__(self, other):
        RegularHexagon.operators_check_and_raise(other, '-')
        new_rec =  RegularHexagon(self.side - other.side)
        if new_rec.side < 0:
            return RegularHexagon(0)
        return new_rec
    # -=
    def __isub__(self, other):
        RegularHexagon.operators_check_and_raise(other, '-=')
        new_rec =  RegularHexagon(self.side - other.side)
        if new_rec.side < 0:
            return RegularHexagon(0)
        return new_rec