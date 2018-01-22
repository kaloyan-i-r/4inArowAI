from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import pickle

# Initialize ANN classifier
# Number of samples in test set: 360 
mlp = None
import pickle
with open("trained_data",'rb') as saved_file:
    mlp = pickle.load(saved_file)
# predict results from the test data

def predict(board):
    return mlp.predict(board)[0]


def main():
    import numpy as np
    print(predict(np.array([[-1,  1,  1,  1, - 1,  1,  1, - 1,  1,  1, - 1,  1, - 1,  1, - 1,  0,  1,  1,
                   - 1, - 1, - 1,  1,  0, - 1, - 1, - 1,  1, - 1,  0,  0,  1, - 1,  1, - 1,  1,  0,
                   0,  1, - 1, - 1, - 1,  1,]])))
    pass

if __name__ == '__main__':
    main()
