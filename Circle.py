from Shapes import Shape
import  math

class Circle(Shape):
    def __init__(self, koter, radious):
        try:
            float(koter), float(radious)
        except Exception:
            raise ValueError("you can enter only numbers!")

        super().__init__()
        self.koter = koter
        self.radious = radious


    def get_area(self):
        return (math.pi * self.radious) ** 2
    def get_perimeter(self):
        return 2 * self.radious * math.pi

    def __repr__(self):
        return f"Circle(koter= {self.koter}, radious = {self.radious})"

    @staticmethod
    def operators_check_and_raise(other, operator):
        if not isinstance(other, Circle):
            raise TypeError(f"operator {operator} is only between Circle and Circle")

    # >=
    def __ge__(self, other):
        Circle.operators_check_and_raise(other, '>=')
        return self.get_area() >= other.get_area()
    # >
    def __gt__(self, other):
        Circle.operators_check_and_raise(other, '>')
        return self.get_area() > other.get_area()
    # <
    def __lt__(self, other):
        Circle.operators_check_and_raise(other, '<')
        return self.get_area() < other.get_area()
    # <=
    def __le__(self, other):
        Circle.operators_check_and_raise(other, '<=')
        return self.get_area() <= other.get_area()
    # ==
    def __eq__(self, other):
        Circle.operators_check_and_raise(other, '==')
        return self.get_area() == other.get_area()
    # !=
    def __ne__(self, other):
        Circle.operators_check_and_raise(other, '!=')
        return self.get_area() != other.get_area()

    # +
    def __add__(self, other):
        Circle.operators_check_and_raise(other, '+')
        return Circle(self.koter + other.koter, self.radious + other.radious)
    # +=
    def __iadd__(self, other):
        Circle.operators_check_and_raise(other, '+=')
        return Circle(self.koter + other.koter, self.radious + other.radious)
    # -
    def __sub__(self, other):
        Circle.operators_check_and_raise(other, '-')
        new_cir =  Circle(self.koter - other.koter, self.radious - other.radious)
        if new_cir.radious < 0 or new_cir.koter < 0:
            return Circle(0,0)
        return new_cir
    # -=
    def __isub__(self, other):
        Circle.operators_check_and_raise(other, '-=')
        new_cir =  Circle(self.koter - other.koter, self.radious - other.radious)
        if new_cir.radious < 0 or new_cir.koter < 0:
            return Circle(0,0)
        return new_cir