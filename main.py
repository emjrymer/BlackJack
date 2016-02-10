
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

    def get_value(self, hand):
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

    def create_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one())
        return hand

deck = Deck()
deck_creation = deck.make_deck()
hit_one = deck.give_one()
print(deck_creation)
hand_creation = deck.create_hand()
print(hand_creation)
hand_value = deck.get_value(hand_creation)
print(hand_value)


class Player:

    def __init__(self):
        # self.hit =
        # self.stay =
        # self.bust =
        self.hand = hand_creation
        # self.turn =
        self.value = hand_value

    def player_hand(self):
        return self.value

    def show_player_hand(self):
        return self.hand

    def player_hit(self):
       want_hit = input("Do you want to hit? Enter y or n ")
       while True:
           if want_hit == "y":
               print("You've chosen to hit. ")
               return hit_one

           elif want_hit == "n":
               print("You've chosen to stand. ")
               break

    def bust(self):
        if hand_value <= 21:
            play_on = True
        else:
            play_on = False
        return play_on

player = Player()
value_player_hand = player.player_hand()
show_player_hand = player.show_player_hand()

print(player.player_hit())

