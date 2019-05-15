from typing import List

tablica: List[str] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def board():
    print(tablica[0:3])
    print(tablica[3:6])
    print(tablica[6:9])


def Tic_Tac_Toe():
    print('Welcome to Tic Tac Toe Game! You are playing on a 3x3 board. Have fun! :)\n')
    player1 = input('Player 1\nPlease tell me if you prefer to use X or O: ')

    if player1.lower() == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
    print('\n' * 3)
    print(f'Player 2 is playing with {player2.upper()}')
    for t, u in enumerate(tablica):
        entry = int(input('Podaj numer miejsca(1-9): '))
        for ind, val in enumerate(tablica):
            if entry == ind and t % 2 == 0:
                print('\n'*100)
                tablica[ind - 1] = player1.upper()
            elif entry == ind and t % 2 != 0:
                print('\n'*100)
                tablica[ind - 1] = player2.upper()
            else:
                continue
        board()
        if tablica[0] == tablica[1] == tablica[2] == 'X' or tablica[3] == tablica[4] == tablica[5] == 'X' or tablica[
            6] == tablica[7] == tablica[8] == 'X' or tablica[0] == tablica[4] == tablica[8] == 'X' or tablica[2] == \
                tablica[4] == tablica[6] == 'X' or tablica[0] == tablica[3] == tablica[5] == 'X' or tablica[1] == \
                tablica[4] == tablica[7] == 'X' or tablica[2] == tablica[5] == tablica[8] == 'X':
            print('X has won!')
            break
        elif tablica[0] == tablica[1] == tablica[2] == 'O' or tablica[3] == tablica[4] == tablica[5] == 'O' or tablica[
            6] == tablica[7] == tablica[8] == 'O' or tablica[0] == tablica[4] == tablica[8] == 'O' or tablica[2] == \
                tablica[4] == tablica[6] == 'O' or tablica[0] == tablica[3] == tablica[5] == 'O' or tablica[1] == \
                tablica[4] == tablica[7] == 'O' or tablica[2] == tablica[5] == tablica[8] == 'O':
            print('O has won!')
            break
Tic_Tac_Toe()