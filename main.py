import random


class Deck:

    def __init__(self):
        self.suit = ['spades', 'hearts', 'diamonds', 'clubs']
        self.val = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.deck = []
        create

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


def game():

    game_on = 'y'

    while game_on == 'y':

        deck = Deck()
        deck.make_deck()
        player = Player()
        print(player.player_hit())
        if player.value > 21:
            game_on = 'n'
        dealer = Dealer()
        print(dealer.dealer_hit())
        if player.value > 21:
            print("Player:  LOsERr!  \nDealer:  WINS!!\nHow embarrassing..")

        elif player.value == 21:
            print("Player:  BLACKJACK!!  \nDealer:  Loses!\nAdd Black Jack skills to your Resume right next to your Loser occupation.")
            break
        elif player.value <= 21 and dealer.value <= 21:
            if player.value > dealer.value:
                print("Player Wins!!  But it doesn't matter. \nDealer loses \n  ")
                game_on = 'n'
            elif player.value == dealer.value:
                print("PUSH IT!! Push it real good. \nGood luck figuring that one out.")
                game_on = 'n'
            else:
                print("Dealer: Wins!!  like usual \nPlayer: loses.")
                game_on = 'n'
        elif player.value <= 21 and dealer.value > 21:
            print("Player Wins!! You are one lucky person. \nDealer loses")
            game_on = 'n'
        elif dealer.value == 21:
            print("Dealer:  BLACKJACK!!  \nPlayer:  loses!  Are you really surprised?")
            game_on = 'n'
        elif dealer.value > 21:
            print("Dealer:  LOSER!  What an idiot \nPlayer:  Winner!!!")
            game_on = 'n'
        elif player.value > 21 and dealer.value > 21:
            print("No Winner, but TWO LOSERS!")
            game_on = 'n'

    else:
        print("The game is over.")
        game_on = input("Do you want to play again? y/n ").lower
        if game_on == 'y':
            game()
        else:
            pass
game()
