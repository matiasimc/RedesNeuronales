from Opts import *
from Network import *
from DatasetParser import *
import random as rd
import matplotlib.pyplot as plt

data_set = parse_dataset("dataset/fertility.csv")
rd.shuffle(data_set)

training_set = data_set[:int(len(data_set)*0.7)]
test_set = data_set[int(len(data_set)*0.3):]

opts = Opts()

opts.iterations = 1
opts.input_size = len(data_set[0]["input"])
opts.output_size = 2

samples = range(1,70)
learning_rates = [float(i)/10 for i in range(1,11)]
layers = [[1], [2,2]]
opts.hidden_layers = [1]

exp = []

for hl in layers:
    opts.hidden_layers = hl
    e = []
    for lr in learning_rates:
        l = []
        opts.learningRate = lr
        f = open('output/prediction2_'+str(lr)+'.txt', 'w')
        for s in samples:
            res = 0.0
            for i in range(100):
                correct_ans = 0.0
                network = NeuralNetwork(opts)
                network.learn(rd.sample(training_set, s))
                for t in rd.sample(test_set, 20):
                    p = network.predict(t["input"])
                    ans = t["output"].index(max(t["output"]))
                    if p == ans:
                        correct_ans += 1.0
                res += correct_ans/20.0
            l.append(res/100.0)
            f.write(str(res/100.0)+'\n')
        e.append((l, lr))
        f.close()
    exp.append(e)

for (i,e) in enumerate(exp):
    plt.subplot(212)
    for d in e:
        plt.plot(range(69), d[0], '-', label=str(d[1]))
    plt.xlabel('Cantidad de entrenamiento')
    plt.ylabel('Tasa de aciertos')
    plt.ylim(ymin=0.4)
    plt.xlim(xmin=0)
    plt.grid(True)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig("output/exp"+str(i+1)+".png")
    plt.clf()
