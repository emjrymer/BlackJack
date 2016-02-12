from deck import Deck


class Dealer:

    def __init__(self):
        self.hand = deck.create_dealer_hand()
        self.value = deck.get_dealer_value(self.hand)

    def show_dealer_hand(self):
        return self.hand

    def dealer_hand(self):
        return self.value

    def dealer_hit(self):
        print(self.hand, self.value)
        while True:
            if self.value == 21:
                return "\n******************* \n Dealer BLACKJACK!! \n   go figure\n******************** \n"
            elif self.value > 17 and self.value < 21:
                return "\n              ****************** \n  Dealer stands, may the odds be ever in your favor.\n              ****************** \n"
            elif self.value > 21:
                return "\n****************** \n Dealer busts!  What an idiot! \n******************** \n"
            print("***Dealer Hits***")
            self.hand.append(deck.give_one_dealer())
            self.value = deck.get_dealer_value(self.hand)
            print(self.hand, self.value)