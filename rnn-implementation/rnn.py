from datetime import datetime
import numpy as np
import sys
from layers import RNNLayer
from activation-functions import Softmax

class Model:
    def __init__(self, word_dim, hidden_dim=100, bptt_truncate=4):
        self.word_dim = word_dim
        self.hidden_dim = hidden_dim
        self.bptt_truncate = bptt_truncate
        self.wax = np.random.uniform(-np.sqrt(1. /word_dim),\
             np.sqrt(1. /word_dim), (hidden_dim, word_dim))
        self.waa = np.random.uniform(-np.sqrt(1. /hidden_dim),\
             np.sqrt(1. /hidden_dim), (hidden_dim, hidden_dim))
        self.way = np.random.uniform(-np.sqrt(1. /hidden_dim),\
             np.sqrt(1. /hidden_dim), (word_dim, hidden_dim))

    def forward_propogation(self,x):

        T = len(x)
        layers = []
        self.prev_a = np.zeros(self.hidden_dim)

        for t in T:
            layer = RNNLayer()
            input = np.zeros(self.word_dim)
            input[x[t]] = 1
            layer.foward(input, prev_a, self.waa, self.wax, self.way)
            prev_a = a
            layers.append(layer)
        return layers

    def predict(self,x):
        output = Softmax()
        layers = self.forward_propogation(x)
        return [ np.argmax(output.predict(layer.mulya)) for layer in layers]        

    ## Loss for each step i.e, each layer of RNN
    def calculate_loss(self,x, y):

        ## Check if length of input and output is same or not
        assert len(y) == len(x)
        
        output = Softmax()
        layers = forward_propogation(x)

        ## Initialize loss with 0
        loss =0

        ## Iterating over layers 
        for i, layer in enumerate(layers):
            loss += output.loss(layer.mulya, y[i])

        return loss/float(len(y))

## We will have N training examples so iterate over all examples to calculate loss
    def calculate_total_loss(self,X,Y):
        loss = 0.0

        for i in range(len(Y)):
            loss += self.calculate_loss(X[i], Y[i])

        return loss/float(len(Y))

