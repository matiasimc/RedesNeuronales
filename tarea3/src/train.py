from RNN2 import *
from build_data import *
import signal

continue_training = False

def initial_generation(N):
    generation = []
    for i in range(N):
      rnn = RNN()
      generation.append(rnn)
    return generation

def train(nn, epoch = 1):
    hprev = np.zeros((data.hidden_layer, 1))
    generation = initial_generation(data.population)
    for e in range(epoch):
        it = 0
        print ">>> Entrenando en epoch "+str(e+1)
        for v in data.verse:
            it += 1
            inputs = [data.char_to_index[c] for c in v[:-1]]
            targets = [data.char_to_index[c] for c in v[1:]]
            forwards = [rnn.forward(inputs, targets, hprev) for rnn in generation]
            generation, sel = nn.genetic_backward(inputs, targets, generation, [x['loss'] for x in forwards])
            hprev = sel[0].forward(inputs, targets, hprev)['hidden']
            if it%1000 == 0:
                samplei = sel[0].sample(inputs[0], 50, hprev)
                txt = ''.join(data.index_to_char[c] for c in samplei)
                print "==Sample=="
                print txt
            nn.WXH = sel[0].WXH
            nn.WHH = sel[0].WHH
            nn.WHY = sel[0].WHY
    np.save("parameters/WXH.npy", nn.WXH)
    np.save("parameters/WHH.npy", nn.WHH)
    np.save("parameters/WHY.npy", nn.WHY)
    np.save("parameters/bH.npy", nn.bH)
    np.save("parameters/bY.npy", nn.bY)

rnn = RNN(continue_training)
signal.signal(signal.SIGINT, rnn.signal_handler)
train(rnn, epoch = data.epoch)

