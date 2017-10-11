import numpy as np
from build_data import *
import sys
import signal

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
        return loss, xs, hs, ps
    
    '''
    Paso backward propagation. Se calculan las gradientes de los parametros.
    '''
    def backward(self, inputs, targets, xs, hs, ps):
        dWXH, dWHH, dWHY = np.zeros_like(self.WXH), np.zeros_like(self.WHH), np.zeros_like(self.WHY)
        dbH, dbY = np.zeros_like(self.bH), np.zeros_like(self.bY)
        dHnext = np.zeros_like(hs[0])
        for t in reversed(xrange(len(inputs))):
            dy = np.copy(ps[t])
            dy[targets[t]] -= 1
            dWHY += np.dot(dy, hs[t].T)
            dbY += dy

            dh = np.dot(self.WHY.T, dy) + dHnext
            dhraw = (1 - hs[t] ** 2) * dh
            dbH += dhraw

            dWXH += np.dot(dhraw, xs[t].T)
            dWHH += np.dot(dhraw, hs[t-1].T)

            dhnext = np.dot(self.WHH.T, dhraw)

        for d in [dWXH, dWHH, dWHY, dbH, dbY]:
            np.clip(d, -5, 5, out=d)

        return dWXH, dWHH, dWHY, dbH, dbY, hs[len(inputs)-1]
    
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
    Metodo que entrena la RNN y guarda los parametros al terminar
    '''
    def train(self, epoch = 1):
        for e in range(epoch):
            it = 0
            print ">>> Entrenando en epoch "+str(e+1)
            hprev = np.zeros((data.hidden_layer, 1))
            mWXH, mWHH, mWHY = np.zeros_like(self.WXH), np.zeros_like(self.WHH), np.zeros_like(self.WHY)
            mbH, mbY = np.zeros_like(self.bH), np.zeros_like(self.bY)
            smooth_loss = -np.log(1.0/data.vocab_size)*20
            for v in data.verse:
                it += 1
                inputs = [data.char_to_index[c] for c in v[:-1]]
                targets = [data.char_to_index[c] for c in v[1:]]
                if it%1000 == 0:
                    samplei = self.sample(inputs[0], 50, hprev)
                    txt = ''.join(data.index_to_char[c] for c in samplei)
                    print "==Sample=="
                    print txt
                loss, xs, hs, ps = self.forward(inputs, targets, hprev)
                dWXH, dWHH, dWHY, dbH, dbY, hprev = self.backward(inputs, targets, xs, hs, ps)
                smooth_loss = smooth_loss * 0.999 + loss * 0.001
                for p, d, m in zip([self.WXH, self.WHH, self.WHY, self.bH, self.bY],
                                    [dWXH, dWHH, dWHY, dbH, dbY],
                                    [mWXH, mWHH, mWHY, mbH, mbY]):
                    m += d ** 2
                    p += -data.learning_rate*d/np.sqrt(m+1e-8)
        np.save("parameters/WXH.npy", self.WXH)
        np.save("parameters/WHH.npy", self.WHH)
        np.save("parameters/WHY.npy", self.WHY)
        np.save("parameters/bH.npy", self.bH)
        np.save("parameters/bY.npy", self.bY)
    
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
