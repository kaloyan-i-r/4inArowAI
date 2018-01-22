from board import *
import random
import ai
import ai_trained as ait
import os.path
import pickle
save_file_name = 'self_training_data'

def loaddata():
    if os.path.isfile(save_file_name):
        return pickle.load(open(save_file_name, 'rb'))
    else:
        return {'data':[],'target':[]}

def savedata(board,move):
    training_data = loaddata()
    training_data['data'].append(board[0])
    training_data['target'].append(move)
    pickle.dump(training_data,open(save_file_name,'wb'))

def main():
    playboard = generate_board(0)[0]
    print_board(playboard)
    player = 0
    for i in range(48):
        if i % 2 == 0:
            player = 1
            move = int(input("move:"))
            # savedata(playboard,move)
        else:
            player = -1
            # move = random.randint(0,6)
            move = ai.predict(playboard)
            # weighted_moves = get_weighted_moves(playboard)
            # print(weighted_moves)
            # move = best_move(weighted_moves)
            # move = ait.predict(playboard)
            print(f'ai move: {move}')
        if check_if_winning_move(player,playboard,move):
            print_board(apply_move(playboard, move, player))
            print(f"GAME OVER player {player} wins!")
            return
        playboard = apply_move(playboard, move,player)
        print_board(playboard)
    pass

if __name__ == '__main__':
    main()
