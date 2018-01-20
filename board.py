import numpy
import math,time,copy
from random import *
from const import *

W = 7
H = 6

def print_board(board):
    if board is None:
        print('no board!')
        return
    print('--0--1--2--3--4--5--6--')
    for i in range(H):
        for j in range(W):
            value = board[0,H*W-(W-j + i*W)]
            symbol = symbols[str(int(value))]
            print(f'  {symbol}', end="")
        print('')
    print('-----------------------')
def board_str(board):
    return string_diag(board[0])

def check_board_for_winner(board):
    board_string = board_str(board)
    lines = []
    for i in range(H):
        tmp_line = ''
        for j in range(W):
            tmp_line += symbols[str(int(board[0][j+i*W]))]
        lines.append(tmp_line)
    for i in range(W):
        tmp_line = ''
        for j in range(H):
            tmp_line += symbols[str(int(board[0][j*W + i]))]
        lines.append(tmp_line)
    for line in lines:
        if 'AAAA' in line or 'BBBB' in line:
            raise NameError('winner :/')


def increment_board(board):
    player = get_player_by_board(board)
    weighted_moves = get_weighted_moves(board, True)
    boards_increment = []
    if len(weighted_moves.keys()) > 0:
        optimal_move_value = max(weighted_moves.values())
        optimal_positions = []
        for position, weight in weighted_moves.items():
            if weight == optimal_move_value:
                optimal_positions.append(position)
        for move in optimal_positions:
            new_board = copy.copy(board)
            apply_move(new_board, move, player)
            try:
                check_board_for_winner(new_board)
            except NameError:
                weighted_moves = get_weighted_moves(board, True, True)
                print(f'player:{player} / move:{move} / ')
                print(weighted_moves)
                print(move)
                print_board(board)
                print_board(new_board)
                raise NameError('end')

            boards_increment.append(new_board)
    else:
        return None
    return boards_increment

def generate_board(moves):
    board = numpy.empty( (1, H*W,))
    board[:] = 0
    for i in range(moves):
        player = get_player(i)
        possible_moves = get_possible_moves(board)
        weighted_moves = evaluate_moves(board,possible_moves,player)
        if len(weighted_moves.keys()) > 0:
            optimal_move_value = max(weighted_moves.values())
            optimal_positions = []
            for position, weight in weighted_moves.items():
                if weight == optimal_move_value:
                    optimal_positions.append(position)
            move = sample(optimal_positions,1)[0]
            apply_move(board,move,player)
        else:
            return None
    return board

def apply_move(board,move,player):
    board[0,find_position(board,move)] = player
    return board


def get_possible_moves(board):
    moves = []
    for i in range(7):
        if find_position(board,i) is not None:
            moves.append(i)
    return moves


def filter_winning_moves(player, board, moves, debug=False):
    filtered_moves = []
    for move in moves:
        if not check_if_winning_move(player, board, move, debug):
            filtered_moves.append(move)
    return filtered_moves


def check_if_winning_move(player, board, move, debug=False):
    calculated_diagonals = generate_diagonals(board,move)
    if debug: print(f'move: {move} / calculated diagonals: {calculated_diagonals}')
    for diagonal in calculated_diagonals:
        str_diag = string_diag(diagonal, player)
        if debug: print(f'str_diag: {str_diag}')
        if symbols[str(abs(player))]*3 in str_diag:
            return True
    return False


def find_position(board,move):
    for i in range(H):
        position = move + W*i
        pos_value = board[0,position]
        if pos_value == 0:
            return position
    return None


def evaluate_moves(board,moves,player):
    weighted_moves = {}
    for move in moves:
        weighted_moves[move] = cost(board,move,player)
    return weighted_moves


def cost(board,move,player):
    diagonals = generate_diagonals(board,move)
    weights = []
    for diag in diagonals:
        # print(string_diag(diag))
        weights.append(surrounding_options[string_diag(diag,player)])
    return sum(weights)


def get_player_by_board(board):
    empty_spaces = (board[0] == 0).sum()
    current_move = H * W - empty_spaces
    return get_player(current_move)


def get_weighted_moves(board, filter_winning=False, debug=False):
    empty_spaces = (board == 0).sum()
    current_move = H * W - empty_spaces + 1
    player = get_player_by_board(board)
    possible_moves = get_possible_moves(board)
    if debug: print(f'possible_moves: {possible_moves}')
    if filter_winning:
        possible_moves = filter_winning_moves(player, board, possible_moves, debug)
    if debug: print(f'filtered_possible_moves: {possible_moves}')
    return evaluate_moves(board, possible_moves, player)


def generate_diagonals(board,move):
    position = find_position(board,move)
    x,y = position % 7,position // 7
    correct_neighbours = []
    for diagonal in diagonals:
        temp_neighbour = []
        for x_delta,y_delta in diagonal:
            temp_x,temp_y = x_delta + x, y_delta +y
            temp_position = temp_x+temp_y*W
            if temp_x < 0 or W <= temp_x or temp_y < 0 or H <= temp_y or temp_position < 0 or temp_position >= (H*W):
                temp_neighbour.append(-2)
            else:
                temp_neighbour.append(board[0,int(temp_position)])
        correct_neighbours.append(temp_neighbour)
    return correct_neighbours

def get_player(move_number):
    return -1 if move_number % 2 == 1 else 1

def vectorized_moves(moves):
    max_weight = max(moves.values())
    print(max_weight)
    vect_moves = []
    for i in range(W):
        if i in moves and moves[i] == max_weight:
            vect_moves.append(1)
        else:
            vect_moves.append(0)
    return numpy.array(vect_moves)


def generate_boards(moves):
    boards = {}
    empty_board = generate_board(0)
    boards[board_str(empty_board)] = empty_board
    count_all = 0
    prev_tier_boards = [empty_board]
    cur_tear_boards = []
    for i in range(1, moves+1):
        start_time = time.time()
        count_collisions = 0
        # print(prev_tier_boards)
        # sample_number = int(math.sqrt(len(prev_tier_boards)))
        # print(sample_number)
        # sample_boards = sample(prev_tier_boards, sample_number)
        # for board in sample_boards:
        for board in prev_tier_boards:
            temp_tear_boards = increment_board(board)
            for new_board in temp_tear_boards:
                board_string = board_str(new_board)
                count_all += 1
                if board_string in boards:
                    count_collisions += 1
                else:
                    boards[board_string] = new_board
                    # if count_collisions > len(cur_tear_boards) / i**3:
                    #     break
            cur_tear_boards.extend(temp_tear_boards)
        print(f'moves: {i} :: generated/max: {len(cur_tear_boards)}/{len(prev_tier_boards)*7} time : {time.time() - start_time}')
        prev_tier_boards = cur_tear_boards
        cur_tear_boards = []
    print(f'all_boards : {len(boards)}')
    return boards

def main():
    gen_boards = generate_boards(36)
    training_set = []
    for str_board in gen_boards:
        board = gen_boards[str_board]
        weighted_moves = get_weighted_moves(board)
        training_set.append([board,vectorized_moves(weighted_moves)])
        print(weighted_moves)
        print_board(board)
    print(len(training_set))
    import pickle
    with open("training_set_data",'wb') as set_file:
        pickle.dump(training_set,set_file)
        pass

if __name__ == '__main__':
    main()