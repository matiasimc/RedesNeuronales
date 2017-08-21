import unittest
from perceptron import *

combinations = [(0,0), (1,1), (1,0), (0,1)]

class TestOr(unittest.TestCase):
    def testAll(self):
        for c in combinations:
            assert perceptronOr.calculate_output(c[0],c[1]) == (c[0] or c[1])

class TestAnd(unittest.TestCase):
    def testAll(self):
        for c in combinations:
            assert perceptronAnd.calculate_output(c[0],c[1]) == (c[0] and c[1])

class TestNand(unittest.TestCase):
    def testAll(self):
        for c in combinations:
            assert perceptronNand.calculate_output(c[0],c[1]) == (not (c[0] and c[1]))


class TestSum(unittest.TestCase):
    def testAll(self):
        for c in combinations:
            r1 = (not ((c[0]) and (c[1])))
            r2 = (not ((c[0]) and r1))
            r3 = (not (r1 and (c[1])))
            expected_sum = (not (r2 and r3))
            expected_carry = (not (r1 and r1))
            assert perceptronSum.calculate_output(c[0], c[1]) == (expected_sum, expected_carry)

if __name__ == "__main__":
    unittest.main() # run all tests
