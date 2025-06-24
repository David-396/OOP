from Shapes import Shape

class RegularHexagon(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side


    def get_area(self):
        return ((3*(3**0.5)) / 2) * self.side ** 2