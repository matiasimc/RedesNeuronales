import numpy as np
from RNN2 import *
import random as rd

'''
En este caso el fitness es inverso (mayor valor, peor especimen)
'''
def fitness(generation, losses):
    return losses

def selection(generation, fitness):
    sort = sorted(zip(generation, fitness), key=lambda tup: tup[1])
    return [x[0] for x in sort[:len(sort)/4]]

ope = np.vectorize(lambda x,y : np.random.choice([x, y]))

def reproduce(N, s):
    newgen = []
    for i in range(N):
        parents = np.random.choice(s, size=2)
        WXHcross = ope(parents[0].WXH, parents[1].WXH)
        WHHcross = ope(parents[0].WHH, parents[1].WHH)
        WHYcross = ope(parents[0].WHY, parents[1].WHY)
        bHcross = ope(parents[0].bH, parents[1].bH)
        bYcross = ope(parents[0].bY, parents[1].bY)
        parents[0].WXH = np.array([[np.random.choice([y, y*rd.random()], p=[0.8, 0.2]) for y in x] for x in WXHcross])
        parents[0].WHH = np.array([[np.random.choice([y, y*rd.random()], p=[0.8, 0.2]) for y in x] for x in WHHcross])
        parents[0].WHY = np.array([[np.random.choice([y, y*rd.random()], p=[0.8, 0.2]) for y in x] for x in WHYcross])
        parents[0].bH = bHcross.reshape(len(bHcross),1)
        parents[0].bY = bYcross.reshape(len(bYcross),1)
        newgen.append(parents[0])
    return newgen

