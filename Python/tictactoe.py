character1 = ''
character2 = ''
table_slots = ['','1','2','3','4','5','6','7','8','9']
turn = 1
choice = 0
endgame = False
selected = []

def display_board(n):
    print(f'''\n
             \t\t\t*\t\t*\t\n
             \t\t{n[7]}\t*\t{n[8]}\t*\t{n[9]}\n
             \t\t\t*\t\t*\t\n
             ****************************************************\n
             \t\t\t*\t\t*\t\n
             \t\t{n[4]}\t*\t{n[5]}\t*\t{n[6]}\n
             \t\t\t*\t\t*\t\n
             ****************************************************\n
             \t\t\t*\t\t*\t\n
             \t\t{n[1]}\t*\t{n[2]}\t*\t{n[3]}\n
             \t\t\t*\t\t*\t\n''')

def start_game():
    global character1
    global character2
    global table_slots

    character1 = input('Would you like to be X or O? ')
    character1 = character1.upper()
    if character1 == "X":
        character2 = 'O'
    else:
        character2 = "X"
    display_board(table_slots)
    while not endgame:
        play_game()

def play_game():
    global turn
    global table_slots
    global character1
    global character2
    global endgame
    global selected

    choice = int(input(f'Player {turn}, please make your move. [1-9]'))
    if turn == 1 and choice not in selected:
        selected.append(choice)
        table_slots[choice] = character1
        if check_win(table_slots) == True:
            display_board(table_slots)
            print(f'{character1} Wins!')
            playagain()
            pass
        turn += 1
    elif turn == 2 and choice not in selected:
        selected.append(choice)
        table_slots[choice] = character2
        if check_win(table_slots) == True:
            display_board(table_slots)
            print(f'{character1} Wins!')
            playagain()
            pass
        turn -= 1
    print(table_slots)
    display_board(table_slots)


def check_win(n):
    return ((n[1] == n[2] and n[2] == n[3]) or
       (n[4] == n[5] and n[5] == n[6]) or
       (n[7] == n[8] and n[8] == n[9]) or
       (n[1] == n[4] and n[4] == n[7]) or
       (n[2] == n[5] and n[5] == n[8]) or
       (n[3] == n[6] and n[6] == n[9]) or
       (n[1] == n[5] and n[5] == n[9]) or
       (n[7] == n[5] and n[5] == n[3]))

def playagain():
    global endgame
    global table_slots
    global selected

    play = input("Would you like to play again? [Yes/No]")
    if play.lower() == 'yes':
        selected = []
        table_slots = ['','1','2','3','4','5','6','7','8','9']
        start_game()
    else:
        endgame = True
start_game()
