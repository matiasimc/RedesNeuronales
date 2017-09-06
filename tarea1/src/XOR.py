from Opts import *
from Network import *

opts = Opts()

opts.learningRate = 0.5
opts.iterations = 20000
opts.input_size = 2
opts.output_size = 1
opts.hidden_layers = [3]

network = NeuralNetwork(opts)

data_set_xor = [
{"input": [0.0,0.0], "output": [0.0]},
{"input": [0.0,1.0], "output": [1.0]},
{"input": [1.0,0.0], "output": [1.0]},
{"input": [1.0,1.0], "output": [0.0]}]

data_set_and = [
{"input": [0.0,0.0], "output": [0.0]},
{"input": [0.0,1.0], "output": [0.0]},
{"input": [1.0,0.0], "output": [0.0]},
{"input": [1.0,1.0], "output": [1.0]}]

network.learn(data_set_xor)

print network.calculate([0,0])
print network.calculate([0,1])
print network.calculate([1,0])
print network.calculate([1,1])
