import unittest
import random as rd
from Neuron import *
from Network import *
from Layer import *
from Opts import *

class NeuronTest(unittest.TestCase):
    def setUp(self):
        self.neuron = Neuron(2)

    def testNeuronCreation(self):
        self.assertEqual(len(self.neuron.weights), 2)

class NetworkTest(unittest.TestCase):
    def setUp(self):
        self.opts = Opts()

        self.opts.learningRate = 0.5
        self.opts.iterations = 20000
        self.opts.input_size = 2
        self.opts.layers = [3]

        self.network = NeuralNetwork(self.opts)

    def testNetworkCreation(self):
        self.assertEqual(self.network.learningRate, self.opts.learningRate)
        self.assertEqual(self.network.iterations, self.opts.iterations)
        self.assertEqual(len(self.network.layers), len(self.opts.layers) + 2)

class LayerTest(unittest.TestCase):
    def setUp(self):
        self.weightNumber = 2
        self.neuronNumber = 3
        self.layer = Layer(self.weightNumber, self.neuronNumber)

    def testLayerCreation(self):
        self.assertEqual(len(self.layer.neurons), self.neuronNumber)

    def testNeuronInLayer(self):
        self.assertEqual(len(self.layer.neurons[0].weights), self.weightNumber)

if __name__ == '__main__':
    unittest.main()
