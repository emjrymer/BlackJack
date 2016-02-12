from deck import Deck



class Player:

    def __init__(self):
        self.hand = deck.create_player_hand()
        self.value = deck.get_player_value(self.hand)

    def show_player_hand(self):
        return self.hand

    def player_hand(self):
        return self.value

    def player_hit(self):
        print(self.hand, self.value)
        while True:
            want_hit = input("Do you want to hit? Enter y or n ")
            if want_hit == "y":
                print("  You've chosen to hit. \n =*=*=*=*=*=*=*=*=*=*=*= \n     Your New Hand \n =*=*=*=*=*=*=*=*=*=*=*=")
                self.hand.append(deck.give_one_player())
                print(self.hand)
                self.value = deck.get_player_value(self.hand)
                print(self.value)
                if player.value > 21:
                    print("LOSER! You busted! \n =*=*=*=*=*=*=*=*=*=*=*= \n     Dealer's Turn \n =*=*=*=*=*=*=*=*=*=*=*=")
                elif self.value == 21:
                    return "Player BLACKJACK!! \n =*=*=*=*=*=*=*=*=*=*=*= \n     Dealer's Turn \n =*=*=*=*=*=*=*=*=*=*=*="
            elif want_hit == "n":
                if self.value == 21:
                    print("Player BLACKJACK!! \n =*=*=*=*=*=*=*=*=*=*=*= \n     Dealer's Turn \n =*=*=*=*=*=*=*=*=*=*=*=")
                return "   Player, you've chosen to stand. \n =*=*=*=*=*=*=*=*=*=*=*= \n     Dealer's Turn \n =*=*=*=*=*=*=*=*=*=*=*="
