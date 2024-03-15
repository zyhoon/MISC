class Hexagon():
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 6

h1 = Hexagon(5)
print(h1.perimeter())
