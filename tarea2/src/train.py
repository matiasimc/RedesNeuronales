from RNN2 import *
import signal

continue_training = True

rnn = RNN(continue_training)
signal.signal(signal.SIGINT, rnn.signal_handler)
rnn.train(data.epoch)
