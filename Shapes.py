from abc import abstractmethod


class Shape:
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


    def __str__(self):
        return f"shape {type(self)} , area = {self.get_area()} , perimeter = {self.get_perimeter()}"

    def __new__(cls, *args, **kwargs):
        print(f"__new__ magic method is called | creating a new {cls}")
        inst = object.__new__(cls)
        return inst



