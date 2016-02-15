from player import Player
from deck import Deck
from dealer import Dealer


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
