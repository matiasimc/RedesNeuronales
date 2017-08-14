class LearningPerceptron:
    def __init__(self, bias = 2, w1 = 1, w2 = 1, C = 0.01):
        self.bias = bias
        self.w1 = w1
        self.w2 = w2
        self.C = C
    def train(self, x1, x2, out):
        my_out = x1*self.w1+x2*self.w2 + self.bias >= 0
        delta = out - my_out
        self.w1 = self.w1 + x1*delta*self.C
        self.w2 = self.w2 + x2*delta*self.C
        self.bias = self.bias + delta*self.C
