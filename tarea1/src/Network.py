from Layer import *

class NeuralNetwork:
    def __init__(self, opts):
        self.learningRate = opts.learningRate
        self.iterations = opts.iterations
        self.layers = []
        self.layers.append(Layer(opts.input_size, opts.input_size))
        for (i, c) in enumerate(opts.hidden_layers):
            self.layers.append(Layer(len(self.layers[len(self.layers)-1].neurons), c))
        self.layers.append(OutputLayer(len(self.layers[len(self.layers)-1].neurons), opts.output_size))

    def feed(self, inputs):
        data = inputs
        for l in self.layers:
            data = l.feed(data)

    def backpropagate(self, expected_output):
        for (i,l) in enumerate(reversed(self.layers)):
            if i != 0:
                l.backpropagate(expected_output, self.layers[len(self.layers)-i])
            else:
                l.backpropagate(expected_output, None)


    def update(self, inputs):
        data = inputs
        for l in self.layers:
            data = l.update(data, self.learningRate)

    def learn(self, data_set):
        for i in range(self.iterations):
            for d in data_set:
                self.feed(d["input"])
                self.backpropagate(d["output"])
                self.update(d["input"])

    def calculate(self, test):
        self.feed(test)
        return [n.output for n in self.layers[len(self.layers) -1].neurons]

    def predict(self,test):
        output = self.calculate(test)
        return output.index(max(output))
