from Shapes import Shape
import  math

class Circle(Shape):
    def __init__(self, koter, radious):
        super().__init__()
        self.koter = koter
        self.radious = radious


    def get_area(self):
        return (3.14159 * self.radious) ** 2