class Deck:

    def __init__(self):
        self.suit = ['spades', 'hearts', 'diamonds', 'clubs']
        self.val = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.deck = []

    def make_deck(self):  # this is my deck
        for s in self.suit:
            for v in self.val:
                self.deck.append(v + ', ' + s)
        return self.deck

    def give_one(self):
        card = self.deck.pop()
        return card

    def create_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one())
        return hand

