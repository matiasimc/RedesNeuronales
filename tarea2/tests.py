from learning_perceptron import *
import unittest
import matplotlib.pyplot as plt
import random as rd

class Test:
    def test(self):
        per = LearningPerceptron()
        a = rd.randint(1,10)
        b = rd.randint(1,10)
        total_points = 100
        training_points = 500
        for n in range(0,total_points):
            x = rd.randint(-total_points,total_points)
            y = rd.randint(-total_points,total_points)
            color = y > a*x + b
            real_color = 'r' if color else 'b'
            plt.plot([x], [y], marker='o', color = real_color)
        for n in range(0, training_points):
            x = rd.randint(-total_points,total_points)
            y = rd.randint(-total_points,total_points)
            color = y > a*x + b
            per.train(x,y,color)
        axes = plt.gca()
        axes.set_xlim([-total_points,total_points])
        axes.set_ylim([-total_points,total_points])
        plt.plot(range(-total_points, total_points), [-per.w1*n1 + per.w2 for n1 in range(-total_points, total_points)])
        plt.show()
Test().test()

# class Test(unittest.TestCase):
