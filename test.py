import json, os
import numpy as np
from NeuralPython.Utils import Builders

def loadData():
	path = './data.csv'
	fullPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
	data = np.genfromtxt(fullPath, delimiter = ',')
	xs = data[:, :2]
	ys = data[:, 2]
	train_data = xs[:150], [], ys[:150]
	validation_data = xs[150:], [], ys[150:]
	test_data = [[], [], []]
	return train_data, validation_data, test_data

config = json.load(open("Config.json"))
net = Builders.buildNetwork(config)
mpiTrain = Builders.buildTraining(config)
mpiTrain.setNetwork(net)
mpiTrain.loadData(loadData)
mpiTrain.run()
