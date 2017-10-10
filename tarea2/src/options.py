import numpy as np

VOCABULARY_SIZE = 2500 #8000
HIDDEN_LAYER = 100 #200
BPTT_TRUNCATE = 4 #4
LEARNING_RATE = 0.005 #0.005
EPOCH = 5 #100

def softmax(x):
    xt = np.exp(x - np.max(x))
    return xt / np.sum(xt)
