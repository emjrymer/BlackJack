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
deck_creation = deck.make_deck()
hit_one = deck.give_one_player()
player_hand_creation = deck.create_player_hand()

#print("Your hand: " + str(player_hand_creation))
player_hand_value = deck.get_player_value(player_hand_creation)
#print("Your hand value: " + str(player_hand_value))


class Player:

    def __init__(self):
        self.hand = player_hand_creation
        self.value = player_hand_value

    def show_player_hand(self):
        return self.hand

    def player_hand(self):
        return self.value

    def player_hit(self):
        hand_creation = deck.create_player_hand()
        while True:
            want_hit = input("Do you want to hit? Enter y or n ")
            if want_hit == "y":
                print("You've chosen to hit.")
                hand_creation.append(deck.give_one_player())
                print(hand_creation)
                print(deck.get_player_value(hand_creation))
                if deck.get_player_value(hand_creation) > 21:
                    return "LOSER!"
                elif deck.get_player_value(hand_creation) == 21:
                    return "BLACKJACK!!"

            elif want_hit == "n":
                if deck.get_player_value(hand_creation) == 21:
                    return "BLACKJACK!!"
                print("You've chosen to stand.")
                return hand_creation


player = Player()
show_hand_player = player.show_player_hand()
val_player_hand = player.player_hand()
print(player.player_hit())



class Dealer:

    def __init__(self):
        self.hand = player_hand_creation
        self.value = player_hand_value

    def show_dealer_hand(self):
        return self.hand

    def dealer_hand(self):
        return self.value

    def dealer_hit(self):
        dealer_hand_creation = deck.create_dealer_hand()
        while True:
            print(dealer_hand_creation.append(deck.give_one_dealer()))
            print(dealer_hand_creation)
            print(deck.get_dealer_value(dealer_hand_creation))
            if deck.get_dealer_value(dealer_hand_creation) == 21:
                return "BLACKJACK!!"
            elif deck.get_dealer_value(dealer_hand_creation) > 17:
                if deck.get_dealer_value(dealer_hand_creation) < 21:
                    return "Dealer stands."
            elif deck.get_dealer_value(dealer_hand_creation) > 21:
                return "LOSER!"
            if deck.get_dealer_value(dealer_hand_creation) <= 17:
                return "Dealer stands."

dealer = Dealer()
dealer_hand_creation = deck.create_dealer_hand()
#print("Dealers hand: " + str(dealer_hand_creation))
dealer_hand_value = deck.get_dealer_value(dealer_hand_creation)
#print("Dealer hand value: " + str(dealer_hand_value))
#print(dealer_hand_creation)
#print(deck.create_dealer_hand())
print(dealer.dealer_hit())


'''
counter = 0
players = ["Dealer", "Player"]
index = counter % 2
while True:
    if index == 0:
        "Players Turn"
        player.player_hit()
    else:
        "Computer Turn"
        dealer.dealer_hit()
'''

if
