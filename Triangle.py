from Shapes import Shape

class Triangle(Shape):
    def __init__(self, height, length):
        super().__init__()
        self.height = height
        self.length = length

    def get_area(self):
        return self.height*self.length / 2
