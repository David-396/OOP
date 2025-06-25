from Rectangle import Rectangle
from Square import Square

rec= Rectangle(2,3)
square = Square(3)
print(rec >= square)
print(dir(rec))


w=Rectangle.__new__(Rectangle)
w.length=2
w.height=4
print(w)