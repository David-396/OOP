from Shapes import Shape

class Triangle(Shape):
    def __init__(self, height, length, hypotenuse):
        try:
            float(height), float(length), float(hypotenuse)
        except Exception:
            raise ValueError("you can enter only numbers!")

        super().__init__()
        self.height = height
        self.length = length
        self.hypotenuse = hypotenuse

    def get_area(self):
        return self.height*self.length / 2
    def get_perimeter(self):
        return self.height+self.length+self.hypotenuse

    def __repr__(self):
        return f"Rectangle(height = {self.height}, length = {self.length}, hypotenuse = {self.hypotenuse})"

    @staticmethod
    def operators_check_and_raise(other, operator):
        if not isinstance(other, Triangle):
            raise TypeError(f"operator {operator} is only between Triangle and Triangle")

    # >=
    def __ge__(self, other):
        Triangle.operators_check_and_raise(other, '>=')
        return self.get_area() >= other.get_area()
    # >
    def __gt__(self, other):
        Triangle.operators_check_and_raise(other, '>')
        return self.get_area() > other.get_area()
    # <
    def __lt__(self, other):
        Triangle.operators_check_and_raise(other, '<')
        return self.get_area() < other.get_area()
    # <=
    def __le__(self, other):
        Triangle.operators_check_and_raise(other, '<=')
        return self.get_area() <= other.get_area()
    # ==
    def __eq__(self, other):
        Triangle.operators_check_and_raise(other, '==')
        return self.get_area() == other.get_area()
    # !=
    def __ne__(self, other):
        Triangle.operators_check_and_raise(other, '!=')
        return self.get_area() != other.get_area()

    # +
    def __add__(self, other):
        Triangle.operators_check_and_raise(other, '+')
        return Triangle(self.height + other.height, self.length + other.length , self.hypotenuse + other.hypotenuse)