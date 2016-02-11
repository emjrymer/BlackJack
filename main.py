import random


class Deck:

    def __init__(self):
        self.suit = ['spades', 'hearts', 'diamonds', 'clubs']
        self.val = {'ace': 'ace', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6','7': '7', '8': '8', '9': '9', '10': '10', 'jack': 'jack', 'queen': 'queen', 'king': 'king'}
        self.deck = []

    def make_deck(self):
        for s in self.suit:
            for v in self.val:
                self.deck.append(v + ', ' + s)
        return self.deck

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
deck_creation = deck.make_deck()
hit_one = deck.give_one_player()
hand_creation = deck.create_player_hand()
print("Your hand: " + str(hand_creation))
hand_value = deck.get_player_value(hand_creation)
print("Your hand value: " + str(hand_value))


class Player:

    def __init__(self):
        self.hand = hand_creation
        self.value = hand_value

    def show_player_hand(self):
        return self.hand

    def player_hand(self):
        return self.value

    def player_hit(self):
        want_hit = input("Do you want to hit? Enter y or n ")
        while True:
            if want_hit == "y":
                print("You've chosen to hit. ")
                hand_creation.append(deck.give_one_player())
                print(deck.get_player_value(hand_creation))
                if deck.get_player_value(hand_creation) > 21:
                    return "LOSER!"
                return hand_creation

            elif want_hit == "n":
                print("You've chosen to stand. ")
                break

player = Player()
show_hand_player = player.show_player_hand()
val_player_hand = player.player_hand()
print(player.player_hit())
