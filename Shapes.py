from abc import abstractmethod


class Shape:
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


    def __str__(self):
        return f"shape {type(self)} , area = {self.get_area()}"
