import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
import pickle
np.random.seed(seed=2017)

def predict(board):
    digits = pickle.load(open('self_training_data','rb'))

    X_train = digits['data']
    # print(X_train)
    y_train = digits['target']
    # print(y_train)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)

    mlp = MLPClassifier(activation='logistic', alpha=0.01, batch_size='auto',
                beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
                hidden_layer_sizes=(30,30), learning_rate='constant',
                learning_rate_init=0.01, max_iter=500, momentum=0.9,
                nesterovs_momentum=True, power_t=0.5, random_state=None,
                shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
                verbose=False, warm_start=False)
    mlp.fit(X_train_scaled, y_train)

    return mlp.predict(board)[0]


def main():
    print(predict(np.array([[-1,  1,  1,  1, - 1,  1,  1, - 1,  1,  1, - 1,  1, - 1,  1, - 1,  0,  1,  1,
                   - 1, - 1, - 1,  1,  0, - 1, - 1, - 1,  1, - 1,  0,  0,  1, - 1,  1, - 1,  1,  0,
                   0,  1, - 1, - 1, - 1,  1,]])))
    pass

if __name__ == '__main__':
    main()
