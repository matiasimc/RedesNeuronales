class Layer:
    def __init__(self, n = 1):
        self.neurons = []
        for i in range(0,n):
            self.neurons.append(Neuron())
        self.nextLayer = None

    def backpropagate(self, expected_output):
        for n in self.neurons:
            accum = 0
            for i in range(0,len(self.neurons)):
                for m in self.nextLayer.neurons:
                    accum += m.weights[i]*m.delta
            n.error = accum
            n.calculate_delta()

    def update(self, inputs):
        for n in self.neurons:
            n.update(inputs)


class OutputLayer(Layer):
    def backpropagate(self, expected_output):
        self.neurons[0].error = expected_output - output
        self.neurons[0].calculate_delta()
