from Neuron import *

class Layer:
    def __init__(self, weightNumber, neuronNumber=1):
        self.neurons = [Neuron(weightNumber) for i in range(neuronNumber)]

    def feed(self, inputs):
        outputs = []
        for n in self.neurons:
            outputs.append(n.sigmoid(inputs))
        return outputs

    def backpropagate(self, expected_output, next_layer):
        for (i,n) in enumerate(self.neurons):
            n.error = 0
            for m in next_layer.neurons:
                n.error += (m.weights[i]*m.delta)
            n.calculate_delta()

    def update(self, inputs, learningRate):
        outputs = []
        for n in self.neurons:
            outputs.append(n.update(inputs, learningRate))
        return outputs



class OutputLayer(Layer):
    def backpropagate(self, expected_output, next_layer):
        for (i,n) in enumerate(self.neurons):
            n.error = expected_output[i] - n.output
            n.calculate_delta()
