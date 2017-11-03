import numpy
from random import *
from const import *

W = 7
H = 6

def printBoard(board):
    if board is None:
        print('no board!')
        return
    print('--0--1--2--3--4--5--6--')
    for i in range(H):
        for j in range(W):
            value = board[0,H*W-(W-j + i*W)]
            # print(f'value: {H*W-(W-j + i*W)}')
            if 0 <= value:
                print(f'  {int(value)}', end="")
            else:
                print(f' {int(value)}', end="")
        print('')
    print('-----------------------')


def generateBoard(moves):
    print(f'moves: {moves}')
    board = numpy.empty( (1,H*W,))
    board[:] = 0
    for i in range(moves):
        player = getPlayer(i)
        possible_moves = getPossibleMoves(board)
        not_winning_moves = filterWinningMoves(player,board,possible_moves)
        weighted_moves = evaluateMoves(board,not_winning_moves,player)
        print(f'player: {player} {weighted_moves}')
        printBoard(board)
        if len(not_winning_moves) > 0:
            move = sample(not_winning_moves,1)[0]
            applyMove(board,move,player)
        else:
            print(f'{i} p/nw : {not_winning_moves}/{possible_moves}')
            printBoard(board)
            return None
        # printBoard(board)
    return board

def applyMove(board,move,player):
    board[0,findPosition(board,move)] = player
    return board

def getPossibleMoves(board):
    moves = []
    for i in range(7):
        # print(f'move: {i} / possition: {findPosition(board,i)}')
        if findPosition(board,i) != None:
            moves.append(i)
    return moves

def filterWinningMoves(player,board,moves):
    filtered_moves = []
    for move in moves:
        if not checkIfWinningMove(player,board,move):
            filtered_moves.append(move)
    return filtered_moves

def checkIfWinningMove(player,board,move):
    diagonals = generateDiagonals(board,move)
    for diagonal in diagonals:
        str_diag = stringDiag(diagonal)
        if symbols[str(player)]*3 in str_diag:
            return True
    return False

def findPosition(board,move):
    for i in range(H):
        position = move + W*i
        pos_value = board[0,position]
        if pos_value == 0:
            return position
    return None

def evaluateMoves(board,moves,player):
    weighted_moves = {}
    for move in moves:
        weighted_moves[move] = cost(board,move,player)
    return weighted_moves

def cost(board,move,player):
    diagonals = generateDiagonals(board,move)
    weights = []
    for diag in diagonals:
        weights.append(surrounding_options[stringDiag(diag,player)])
    return max(weights)

def generateDiagonals(board,move):
    position = findPosition(board,move)
    correct_neighbours = []
    for diagonal in diagonals:
        temp_neighbour = []
        for diag_delta in diagonal:
            diag_pos = position + diag_delta
            if diag_pos < 0 or 41 < diag_pos:
                temp_neighbour.append(-2)
            else:
                temp_neighbour.append(board[0,diag_pos])
        correct_neighbours.append(temp_neighbour)
    return correct_neighbours

def getPlayer(move_number):
    return -1 if move_number % 2 == 1 else 1

def main():
    # printBoard(generateBoard(0))
    # printBoard(generateBoard(5))
    # printBoard(generateBoard(10))
    # printBoard(generateBoard(15))
    # printBoard(generateBoard(20))
    # printBoard(generateBoard(25))
    # printBoard(generateBoard(30))
    printBoard(generateBoard(35))
    # printBoard(generateBoard(43))
    pass

if __name__ == '__main__':
    main()