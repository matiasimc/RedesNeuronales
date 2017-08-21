import math

class LearningPerceptron:
    def __init__(self, bias = 2, w1 = 2, w2 = 2, C = 0.01):
        self.bias = bias
        self.w1 = w1
        self.w2 = w2
        self.C = C
    def perceptron_output(self,x1,x2):
        return x1*self.w1+x2*self.w2 + self.bias >= 0
    def sigmoid_output(self,x1,x2):
        return 1.0/(1+math.exp(-(x1*self.w1+x2*self.w2) - self.bias))
    def train(self, x1, x2, out):
        my_out = self.sigmoid_output(x1,x2)
        delta = out - my_out
        self.w1 = self.w1 + x1*delta*self.C
        self.w2 = self.w2 + x2*delta*self.C
        self.bias = self.bias + delta*self.C
