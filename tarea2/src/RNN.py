from build_data import *
from options import *
import numpy as np
import nltk



class RNN:
    def __init__(self, parameters = False):
        # Inicializar parametros de la red neuronal
        self.U = np.random.uniform(-np.sqrt(1./VOCABULARY_SIZE), np.sqrt(1./VOCABULARY_SIZE), (HIDDEN_LAYER, VOCABULARY_SIZE))
        self.V = np.random.uniform(-np.sqrt(1./HIDDEN_LAYER), np.sqrt(1./HIDDEN_LAYER), (VOCABULARY_SIZE, HIDDEN_LAYER))
        self.W = np.random.uniform(-np.sqrt(1./HIDDEN_LAYER), np.sqrt(1./HIDDEN_LAYER), (HIDDEN_LAYER, HIDDEN_LAYER))
        if parameters:
            self.U = np.load("parameters/U.npy")
            self.V = np.load("parameters/V.npy")
            self.W = np.load("parameters/W.npy")

    '''
    Realiza el forward propagation, retornando el estado de las capas ocultas y el output
    '''
    def forward_propagation(self, x):
        # Numero de pasos temporales
        T = len(x)
        # Matriz de hidden layers
        s = np.zeros((T + 1, HIDDEN_LAYER))
        s[-1] = np.zeros(HIDDEN_LAYER)
        # Outputs
        o = np.zeros((T, VOCABULARY_SIZE))
        for t in np.arange(T):
            # La funcion de activacion
            s[t] = np.tanh(self.U[:, x[t]] + self.W.dot(s[t-1]))
            o[t] = softmax(self.V.dot(s[t]))
        return o, s

    '''
    Predice la siguiente palabra
    '''
    def predict(self, x):
        o, s = self.forward_propagation(x)
        return np.argmax(o, axis=1)
    

    '''
    Calcula la perdida, usando cross-entropy loss
    '''
    def total_loss(self, x, y):
        l = 0
        for i in np.arange(len(y)):
            o, s = self.forward_propagation(x[i])
            correct = o[np.arange(len(y[i])), y[i]]
            l += -1*np.sum(np.log(correct))
        return l

    def loss(self, x, y):
        # Divide la perdida total por la cantidad de entrenamiento
        n = np.sum([len(y_i) for y_i in y])
        return self.total_loss(x, y)/N

    '''
    Realiza Backpropagation Through Time (BPTT) con Stochastic Gradient Descent (SGD). 
    Retorna los gradientes de la perdida respecto a los vectores U, V y W
    '''

    def backpropagation(self, x, y):
        T = len(y)
        o, s = self.forward_propagation(x)
        dLdU = np.zeros(self.U.shape)
        dLdV = np.zeros(self.V.shape)
        dLdW = np.zeros(self.W.shape)
        # Regla de la cadena
        delta_o = o
        delta_o[np.arange(len(y)), y] -= 1
        for t in np.arange(T)[::-1]:
            dLdV += np.outer(delta_o[t], s[t].T)
            delta_t = self.V.T.dot(delta_o[t]) * (1 - (s[t] ** 2))
            for bptt_step in np.arange(max(0, t-BPTT_TRUNCATE), t+1)[::-1]:
                dLdW += np.outer(delta_t, s[bptt_step-1])
                dLdU[:,x[bptt_step]] += delta_t
                delta_t = self.W.T.dot(delta_t) * (1 - s[bptt_step-1] ** 2)
        return [dLdU, dLdV, dLdW]

    def sgd_step(self, x, y):
        dLdU, dLdV, dLdW = self.backpropagation(x, y)
        self.U -= LEARNING_RATE*dLdU
        self.V -= LEARNING_RATE*dLdV
        self.W -= LEARNING_RATE*dLdW

    def train(self, x_train, y_train):
        for epoch in range(EPOCH):
            print "Entrenando en la epoch "+str(epoch+1)
            self.sgd_step(x_train, y_train)
        np.save("parameters/U.npy", self.U)
        np.save("parameters/V.npy", self.V)
        np.save("parameters/W.npy", self.W)

    def generate_text(self, wti, itw):
        new_text = [wti["START_POEM"]]
        for i in range(30):
            probabilities, sr = self.forward_propagation(new_text)
            prediction = wti["UNKNOWN_WORD"]
            if prediction == wti["UNKNOWN_WORD"]:
                probabilities[-1][wti["UNKNOWN_WORD"]] = 0
                samples = np.random.multinomial(1, probabilities[-1])
                prediction = np.argmax(samples)
            new_text.append(prediction)
        s = [itw[x] for x in new_text]
        return s


x_train, y_train = get_training_data("data/neruda.csv")
itw, wti = get_most_used_words("data/neruda.csv")
parameters = False 

model = RNN(parameters)
if not parameters: model.train(x_train, y_train)
print model.generate_text(wti, itw)
