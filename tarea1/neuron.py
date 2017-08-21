import math

class Neuron:
    def __init__(self):
        self.weights = []
        self.bias = 0
        self.error = 0
        self.delta = 0
        self.threshold = 0.5
        self.output = 0

    def setWeights(self, w):
        self.weights = w

    def calculate(self, inputs):
        return 1 if self.sigmoid(inputs) > self.threshold else 0

    def sigmoid(self, inputs):
        return 1 / (1 + math.exp(-sum([x*y for x,y in zip(self.weights, inputs)])))

    def transfer_derivate(self):
        return self.output*(1.0 - self.output)

    def calculate_delta(self):
        ret = self.error*self.transfer_derivate()
        self.delta = ret
        return ret

    def update(self, inputs):
        for i in range(0,len(inputs)):
            self.weights[i] += (self.threshold*self.delta*inputs[i])
        self.bias += (self.threshold*delta)
