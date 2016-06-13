import json
import mnist_loader
from NeuralPython.Utils import Builders


config = json.load(open("Config3.json"))
net = Builders.buildNetwork(config)
mpiTrain = Builders.buildTraining(config)
mpiTrain.setNetwork(net)
mpiTrain.loadData(mnist_loader.load_data_wrapper2D)
mpiTrain.run()
