'''
Ejercicio 1 Redes Neuronales y Programacion Genetica
Implementacion de operadores de bit OR, AND, NAND y SUM

Autor: Matias Meneses C.
'''

class Perceptron:
    def __init__(self, bias = 0, w1 = 0, w2 = 0):
        self.bias = bias
        self.w1 = w1
        self.w2 = w2

    # Dados dos bits, calcula el output
    def calculate_output(self, x1, x2):
        return 1 if x1*self.w1 + x2*self.w2 + self.bias > 0 else 0

class Sum:
    def __init__(self):
        self.nand = Perceptron(bias = 3, w1 = -2, w2 = -2)

    # Dados dos bits, calcula la suma y el carry
    def calculate_output(self, x1, x2):
        r1 = self.nand.calculate_output(x1,x2)
        r2 = self.nand.calculate_output(x1,r1)
        r3 = self.nand.calculate_output(r1,x2)
        sumr = self.nand.calculate_output(r2,r3)
        carry = self.nand.calculate_output(r1,r1)
        return sumr, carry

perceptronAnd = Perceptron(bias = -1, w1 = 1, w2 = 1)
perceptronOr = Perceptron(bias = 0, w1 = 1, w2 = 1)
perceptronNand = Perceptron(bias = 3, w1 = -2, w2 = -2)
perceptronSum = Sum()
