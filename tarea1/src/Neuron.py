import random as rd
import math
import numpy as np

class Neuron:
    def __init__(self, weightNumber=1):
        self.error = 0
        self.delta = 0
        self.output = 0
        self.weights = [rd.random()+1 for i in range(weightNumber)]
        self.bias = rd.random()+1

    def sigmoid(self, inputs):
        self.output = (1.0 / (1.0 + math.exp(-sum([x*y for x,y in zip(self.weights, inputs)]) - self.bias)))
        return self.output

    def transfer_derivative(self):
        return self.output*(1.0 - self.output)

    def calculate_delta(self):
        self.delta = self.error*self.transfer_derivative()

    def update(self, inputs, learningRate):
        for (i,w) in enumerate(self.weights):
            self.weights[i] = w + (learningRate*self.delta*inputs[i])
        self.bias += (learningRate*self.delta)
        return self.output
