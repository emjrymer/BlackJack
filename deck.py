import random


class Deck:

    def __init__(self):
        self.suit = ['spades', 'hearts', 'diamonds', 'clubs']
        self.val = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.deck = []

    def make_deck(self):
        for s in self.suit:
            for v in self.val:
                self.deck.append(v + ', ' + s)
        return random.shuffle(self.deck)

    def give_one_player(self):
        card = self.deck.pop()
        return card

    def give_one_dealer(self):
        card = self.deck.pop()
        return card

    def get_player_value(self, hand):
        d = 0
        for card in hand:
            for value in card[0]:
                try:
                    value = int(value)
                    if int(value) == 1:
                        value = 10
                except ValueError:
                    if value == 'a':
                        value = 11
                    elif value in 'jqk':
                        value = 10
            d += value
        return d

    def get_dealer_value(self, hand):
        d = 0
        for card in hand:
            for value in card[0]:
                try:
                    value = int(value)
                    if int(value) == 1:
                        value = 10
                except ValueError:
                    if value == 'a':
                        value = 11
                    elif value in 'jqk':
                        value = 10
            d += value
        return d

    def create_player_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one_player())
        return hand

    def create_dealer_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one_dealer())
        return hand

deck = Deck()
deck.make_deck()