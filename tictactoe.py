#!/usr/bin/env python
__title__ = "Tic Tac Toe"
__author__ = "Monil Kaneria"
__version__ = "1.0.0"
__init_Publish_date__ = "03/17/2020"


def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--' + '    player 1 is {}'.format(player1_marker))
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--' + '    player 2 is {}'.format(player2_marker))
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''
    # keep asking player 1 to choose X or O
    while marker.upper() != 'X' and marker.upper() != 'O':
        print()
        marker = input('Player 1, choose X or O: ')
        print()
    # assign player 2 with the opposite marker
    player1 = marker.upper()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return(player1, player2)


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((mark == board[1] == board[2] == board[3]) or
    (mark == board[4] and mark == board[5] and mark == board[6]) or
    (mark == board[7] and mark == board[8] and mark == board[9]) or
    (mark == board[1] and mark == board[4] and mark == board[7]) or
    (mark == board[2] and mark == board[5] and mark == board[8]) or
    (mark == board[3] and mark == board[6] and mark == board[9]) or
    (mark == board[1] and mark == board[5] and mark == board[9]) or
    (mark == board[3] and mark == board[5] and mark == board[7]))


import random

def choose_first():
    selector = random.randint(0,1)
    if selector == 0:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def player_choice(board):
    check = True
    while check:
        print()
        pos = input('please enter your position from [1 to 9]: ')
        print()

        if pos not in ['1','2','3','4','5','6','7','8','9']:
            print('please enter valid number between [1 to 9]')
        else:
            if not space_check(board, int(pos)):
                print('this position is already filled')
            else:
                pos = int(pos)
                check = False
    return pos

def replay():
    check = True
    while check:
        print()
        play_again = input('Do you want to play again? type YES or NO: ')
        print()
        if play_again.lower() != 'yes' and play_again.lower() != 'no':
            print('please enter either YES or NO')
        else:
            check = False 
    return play_again.lower() == 'yes'


print('Welcome to Tic Tac Toe!')
print()

while True:
    
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' goes first')

    check = True
    while check:
        print()
        start_game = input('are you ready? Enter YES or No: ')
        print()
        if start_game.lower() != 'yes' and start_game.lower() != 'no':
            print('please enter either YES or NO')
        else:
            check = False

    if start_game.lower() == 'yes':
        game_on = True
    else: 
        game_on = False
        
    while game_on:
        if turn == 'player1':
            print()
            print('player 1 \'s turn')
            print()
            display_board(board)
            print()
            choice = player_choice(board)
            place_marker(board, player1_marker, choice)
            
            if win_check(board, player1_marker):
                print()
                display_board(board)
                print()
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(board):
                    print()
                    display_board(board)
                    print()
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player2'
        else:
            print()
            print('player 2 \'s turn')
            print()
            display_board(board)
            print()
            choice = player_choice(board)
            place_marker(board, player2_marker, choice)
            
            if win_check(board, player2_marker):
                print()
                display_board(board)
                print()
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(board):
                    print()
                    display_board(board)
                    print()
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player1'
    
    if not replay():
        break
