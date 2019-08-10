import random
import sys

class Player:
    def __init__(self, cardvalue, chips):
        self.cardvalue = cardvalue
        self.chips = chips
        self.bet = 0

    def hit(self, cards, name, newcard):
        self.cardvalue += get_value(newcard, name)
        print(f"{name} is Holding: {cards}, value: {self.cardvalue}")
        return self.cardvalue

def deal_cards():
    select_card(random.choice(deck), playercards)
    select_card(random.choice(deck), playercards)
    select_card(random.choice(deck), computercards)

    player.cardvalue = (get_value(playercards[0], "player")+get_value(playercards[1], "player"))
    computer.cardvalue = get_value(computercards[0], "computer")

    print(f"Player is holding {playercards}, hand valued at {player.cardvalue}")
    print(f"Dealer is holding {computercards}, hand valued at {computer.cardvalue}")

def select_card(card, cardlist):
    cardlist.append(card)
    deck.remove(card)
    return card

def get_value(str, name):
    value = str.split(" ")
    if value[0].isnumeric():
        return int(value[0])

    elif value[0].lower() == 'ace':
        if name.lower() == player:
            if player.cardvalue + 11 <= 21:
                return 11
            else:
                return 1
        else:
            if computer.cardvalue + 11 <= 21:
                return 11
            else:
                return 1
    else:
        return 10

def start_game():
    print("Welcome to BlackJack!")

    try:
        while True:
            player.bet = int(input("Please place your bet amount (Min bet is $5): "))
            if player.bet > player.chips and player.chips > 5:
                print("Insufficient Chips. Place another bet.")
            elif player.chips < 5:
                print("Insufficient Chips. Please purchase more.")
            elif player.bet < 5:
                print("Minimum bet is $5. Try again.")
            else:
                player.chips -= player.bet
                break
    except:
        print("Please enter a valid number.")
    else:
        print(f"Your bet for ${player.bet} has been placed.")
        print(f"Your chip count is now ${player.chips}")

    print("Dealing out cards...")
    deal_cards()
    check_player_wins()


def initDeck():
    for i in ["Hearts", "Spades", "Clubs", "Diamonds"]:
        for j in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
            deck.append(j+' of '+i)

def check_player_wins():
    if player.cardvalue == 21:
        print("YOU WIN!!")
        playagain()
    else:
        continue_game()

def continue_game():
    while True:
        hit = input("Please press Enter to Hit, or Any other character to Check: ")
        if hit == '':

            if player.hit(playercards, "Player", select_card(random.choice(deck), playercards)) <= 21:
                continue
            else:
                print("Player Bust!")
                break
        else:
            while (computer.cardvalue <= player.cardvalue) and (computer.cardvalue <= 21):

                computer.hit(computercards, "Dealer", select_card(random.choice(deck), computercards))
            if computer.cardvalue == player.cardvalue:
                print("We have a tie")
            elif computer.cardvalue > 21:
                print("Dealer BUST!")
                player.chips += player.bet*2
            elif (computer.cardvalue < player.cardvalue) and (player.cardvalue <= 21):
                print("Player WINS!")
                player.chips += player.bet*2
            else:
                print("Player loses.")
            break

    play_again()

def play_again():
    replay = input("Would you like to play again?: Y or N? ")
    if replay.lower() == 'y':
        if player.chips <= 5:
            print("Not enough chips to play agian. Please purchase more.")
        else:
            deck.clear()
            playercards.clear()
            computercards.clear()
            initDeck()
            start_game()
    else:
        print("Thanks for playing!")


deck = []
playercards = []
computercards = []
initDeck()
player = Player(0, 100)
computer = Player(0,0)
start_game()
