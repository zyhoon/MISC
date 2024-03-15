class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def change_size(self, newside):
        self.side += newside

    def calculate_perimeter(self):
        return self.side * 4

class Rider():
    def __init__(self, name):
        self.name = name
        
class Horse():
    def __init__(self, colour, breed, rider):
        self.colour = colour
        self.breed = breed
        self.rider = rider

r1 = Rider("tom")
pony = Horse("black", "seahorse", r1)

print(pony.rider.name)
