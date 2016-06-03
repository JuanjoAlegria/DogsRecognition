import json
import mnist_loader
from NeuralPython import MPINetwork


config = json.load(open("Config.json"))
net = MPINetwork.buildFromDict(config)
net.loadData(mnist_loader.load_data_wrapper)
net.run()
