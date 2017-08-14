from learning_perceptron import *
import unittest
import matplotlib.pyplot as plt
import random as rd

class Test:
    def test(self):
        a = rd.randint(-10,10)
        b = rd.randint(-10,10)
        limit = 100
        test_redo = 200
        test_points = 80
        fine_list = []
        for i in range(0, test_redo):
            per = LearningPerceptron()
            for n in range(0, test_redo):
                x = rd.randint(-limit,limit)
                y = rd.randint(-limit,limit)
                color = y > a*x + b
                per.train(x,y,color)
            fine = 0
            for n in range(0, test_points):
                x = rd.randint(-limit,limit)
                y = rd.randint(-limit,limit)
                color = y > -per.w1*x + per.w2
                expected = y > a*x + b
                if color == expected:
                    fine += 1
                real_color = 'r' if color else 'b'
                if i == test_points - 1:
                    plt.plot([x], [y], marker='o', color = real_color)
            rate = 1.0*fine/test_points
            fine_list.append(rate)
        axes = plt.gca()
        axes.set_xlim([-limit,limit])
        axes.set_ylim([-limit,limit])
        plt.plot(range(-limit,limit), [-per.w1*n1 + per.w2 for n1 in range(-limit,limit)])
        plt.draw()
        plt.figure()
        axes = plt.gca()
        axes.set_xlim([0,test_redo])
        axes.set_ylim([0,1])
        plt.plot(range(0,test_redo), fine_list)
        plt.draw()
        plt.show()
Test().test()

# class Test(unittest.TestCase):
