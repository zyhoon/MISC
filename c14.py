class Square():

    def __init__(self, length):
        self.length = length

    def __repr__(self):
        side = self.length
        return "{} by {} by {} by {}".format(side, side, side, side)

s1 = Square(29)
s2 = Square(36)

def comparison(s1, s2):
    print(s1 is s2)

comparison(s1, s2)

