import numpy as np
import itertools
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


class Parse:
    def __init__(self, filename):
        self.data = open(filename, 'r').read().encode('utf-8')
        self.verse = ["&".encode('utf-8')+s.encode('utf-8')+"&".encode('utf-8') for s in self.data.split('&')]
        self.chars = list(set(self.data))
        self.data_size = len(self.data)
        self.vocab_size = len(self.chars)
        self.char_to_index = {ch:i for i, ch in enumerate(self.chars)}
        self.index_to_char = {i:ch for i, ch in enumerate(self.chars)}
        self.hidden_layer = 30
        self.learning_rate = 0.1
        self.epoch = 1000
        self.population = 16
