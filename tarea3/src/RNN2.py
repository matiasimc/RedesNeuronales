import numpy as np
from build_data import *
import sys
import signal
from genetic import *

data = Parse('data/neruda.csv')

class RNN:
    def __init__(self, parameters = False):
        self.WXH = np.random.randn(data.hidden_layer, data.vocab_size)*0.01
        self.WHH = np.random.randn(data.hidden_layer, data.hidden_layer)*0.01
        self.WHY = np.random.randn(data.vocab_size, data.hidden_layer)*0.01
        self.bH = np.zeros((data.hidden_layer, 1))
        self.bY = np.zeros((data.vocab_size, 1))
        if parameters:
            self.WXH = np.load('parameters/WXH.npy')
            self.WHH = np.load('parameters/WHH.npy')
            self.WHY = np.load('parameters/WHY.npy')
            self.bH = np.load('parameters/bH.npy')
            self.bY = np.load('parameters/bY.npy')


    '''
    Paso forward. Se calculan los vectores input, hidden, output y la perdida.
    '''
    def forward(self, inputs, targets, hprev):
        xs, hs, ys, ps = {}, {}, {}, {}
        hs[-1] = np.copy(hprev)
        loss = 0
        for t in xrange(len(inputs)):
            xs[t] = np.zeros((data.vocab_size, 1))
            xs[t][inputs[t]] = 1

            hs[t] = np.tanh(np.dot(self.WXH, xs[t]) + np.dot(self.WHH, hs[t-1]) + self.bH)
            ys[t] = np.dot(self.WHY, hs[t]) + self.bY
            ps[t] = np.exp(ys[t]-np.max(ys[t])) / np.sum(np.exp(ys[t]-np.max(ys[t])))
            loss += -np.log(ps[t][targets[t], 0])
        return {'loss': loss, 'probdist': ps, 'hidden': hs[len(inputs)-1]}
    

    '''
    Paso backward usando un algoritmo genetico. Se calcula proxima generacion y la seleccion 
    de la generacion actual de mejor a peor.
    '''
    def genetic_backward(self, inputs, targets, generation, losses):
        f = fitness(generation, losses)
        s = selection(generation, f)
        g = reproduce(len(generation), s)
        return g, s

    
    '''
    Metodos que realizan sampling.
    '''
    def sample(self, seed_index, n, h=np.zeros((data.hidden_layer, 1))):
        x = np.zeros((data.vocab_size, 1))
        x[seed_index] = 1
        string_vector = []
        for t in xrange(n):
            h = np.tanh(np.dot(self.WXH, x) + np.dot(self.WHH, h) + self.bH)
            y = np.dot(self.WHY, h) + self.bY
            p = np.exp(y-np.max(y)) / np.sum(np.exp(y-np.max(y)))
            index = np.random.choice(range(data.vocab_size), p=p.ravel())

            x = np.zeros((data.vocab_size, 1))
            x[index] = 1
            string_vector.append(index)
        return string_vector

    def sample_argmax(self, seed_index, n, h=np.zeros((data.hidden_layer, 1))):
        x = np.zeros((data.vocab_size, 1))
        x[seed_index] = 1
        string_vector = []
        for t in xrange(n):
            h = np.tanh(np.dot(self.WXH, x) + np.dot(self.WHH, h) + self.bH)
            y = np.dot(self.WHY, h) + self.bY
            p = np.exp(y-np.max(y)) / np.sum(np.exp(y-np.max(y)))
            index = np.argmax(p.ravel())

            x = np.zeros((data.vocab_size, 1))
            x[index] = 1
            string_vector.append(index)
        return string_vector

    def sample_hybrid(self, seed_index, n, h=np.zeros((data.hidden_layer, 1))):
        x = np.zeros((data.vocab_size, 1))
        x[seed_index] = 1
        string_vector = []
        prev_char = seed_index
        for t in xrange(n):
            h = np.tanh(np.dot(self.WXH, x) + np.dot(self.WHH, h) + self.bH)
            y = np.dot(self.WHY, h) + self.bY
            p = np.exp(y-np.max(y)) / np.sum(np.exp(y-np.max(y)))
            index = np.random.choice(range(data.vocab_size), p=p.ravel())
            if data.index_to_char[prev_char].isalpha():
                index = np.argmax(p.ravel())
            x = np.zeros((data.vocab_size, 1))
            x[index] = 1
            string_vector.append(index)
            prev_char = index
        return string_vector
    
    
    '''
    Handler que captura ctrl-c y guarda los parametros hasta ese momento
    '''
    def signal_handler(self, signal, frame):
        print "saving..."
        np.save("parameters/WXH.npy", self.WXH)
        np.save("parameters/WHH.npy", self.WHH)
        np.save("parameters/WHY.npy", self.WHY)
        np.save("parameters/bH.npy", self.bH)
        np.save("parameters/bY.npy", self.bY)
        sys.exit()
