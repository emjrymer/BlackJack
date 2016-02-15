from player import Player
from deck import Deck
from dealer import Dealer


def game():

    print("Welcome to BlackJack The Ruthless")
    game_on = input("Do you want to play a game? y/n ")

    while game_on == 'y':
        print("*+*+*+*+*+*+*+*+*+*+*+ \n      New Game \n*+*+*+*+*+*+*+*+*+*+*+ \n Player's Hand")
        deck = Deck()
        deck.make_deck()
        player = Player()
        print(player.player_hit())
        if player.value > 21:
            game_on = input("You busted, game over.  \nDo you want to see the dealers turn? y/n ")
        dealer = Dealer()
        print(dealer.dealer_hit())
        if player.value > 21 and dealer.value > 21:
            print("Player:  LOsERr!!!  \nDealer:  LOsERr!!!\nHow embarrassing..")
            game_on = input("Do you want to play again? y/n ")
        elif player.value == 21:
            print("Player:  BLACKJACK!!  \nDealer:  Loses!\nAdd Black Jack skills to your Resume.")
            game_on = input("Do you want to play again? y/n ")
        elif player.value <= 21 and dealer.value <= 21:
            if player.value > dealer.value:
                print("Player Wins!!  But it doesn't matter. \nDealer loses \n  ")
                game_on = input("Do you want to play again? y/n ")
            elif player.value == dealer.value:
                print("PUSH IT!! Push it real good. \nGood luck figuring that one out.")
                game_on = input("Do you want to play again? y/n ")
            else:
                print("Dealer: Wins!!  like usual \nPlayer: loses.")
                game_on = input("Do you want to play again? y/n ")
        elif player.value <= 21 and dealer.value > 21:
            print("Player Wins!! You are one lucky person. \nDealer loses")
            game_on = input("Do you want to play again? y/n ")
        elif dealer.value == 21:
            print("Dealer:  BLACKJACK!!  \nPlayer:  loses!  Are you really surprised?")
            game_on = input("Do you want to play again? y/n ")
        elif dealer.value > 21:
            print("Dealer:  LOSER!  What an idiot \nPlayer:  Winner!!!")
            game_on = input("Do you want to play again? y/n ")
        elif player.value > 21 and dealer.value < 21:
            print("Dealer Wins, again!!!")
            game_on = input("Do you want to play again? y/n ")

game()