from random import shuffle

class Card():
    suits = ["diamonds", "clubs", "hearts", "spades"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v
        
class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.wins = 0
        self.name = name
        self.card = None

class Game():
    def __init__(self):
        name1 = input("player one's name: ")
        name2 = input("player two's name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "\n{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "\n{} drew {} and {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("\nWelcome to the game of War!")
        while len(cards) >= 2:
            print("\nCurrent Scoreboard - {}:{} and {}:{}".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))
            response = input("\nPress 'q' to quit or any key to play.\n")
            if response == "q":
                break
            else:
                p1c = self.deck.rm_cards()
                p2c = self.deck.rm_cards()
                p1n = self.p1.name
                p2n = self.p2.name
                self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("\nFinal Scoreboard - {}:{} and {}:{}".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))
        print("{} wins the war!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return ("It's a tie!")

game = Game()
game.play_game()

    
    


    
