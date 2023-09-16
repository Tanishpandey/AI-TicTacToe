"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xc=0
    oc=0
    for i in board:
        for j in i:
            if j ==X:
                xc+=1
            elif j == O:
                oc+=1
    if xc ==0:
        return X
    elif xc>oc:
        return O
    else:
        return X 


def actions(board):
    nboardac = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                nboardac.add((i,j))
    return nboardac


def result(board, action):
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board    
    

def winner(board):
    #rows check
    for index1 in board:
        if index1[0] == index1[1] == index1[2] and index1[0] != '.':
            return index1[0]
    #columns check
    for index2 in range(3):
        if board[0][index2] == board[1][index2] == board[2][index2] and board[0][index2] != '.':
            return board[0][index2]
    #Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None
    


def terminal(board):
    if winner(board):
        return True
    for i in board:
        if EMPTY in i:
            return False
    
    return True
    


def utility(board):
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def max_value(board, a, b):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None

    for action in actions(board):
        maxi, _ = min_value(result(board, action), a, b)
        if maxi > v:
            v = maxi
            move = action
        a = max(a, v)
        if v == 1:
            return v, move
        if b <= a:
            break

    return v, move

def min_value(board, a, b):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None

    for action in actions(board):
        #unpacking the tuple
        mini, _ = max_value(result(board, action), a, b)
        if mini < v:
            v = mini
            move = action
        b = min(b, v)
        if v == -1:
            return v, move
        if b <= a:
            break

    return v, move


def minimax(board):

    if terminal(board):
        return None

    if player(board) == X:
        temp_var, move = max_value(board, float('-inf'), float('inf'))
    else:
        temp_var, move = min_value(board, float('-inf'), float('inf'))

    return move




