from Shapes import Shape

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side =side

    def get_area(self):
        return self.side**2

