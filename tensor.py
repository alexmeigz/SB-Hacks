import numpy as np
from conversions import *
from rubix import *

@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.e ** -x)
activation_function = sigmoid

from scipy.stats import truncnorm

def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


class NeuralNetwork:
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate,
                 bias=None
                ):  

        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.lastMove = 12
        
        self.no_of_hidden_nodes = no_of_hidden_nodes
            
        self.learning_rate = learning_rate 
        self.bias = bias
        self.create_weight_matrices()
    
        
    
    def create_weight_matrices(self):
        """ A method to initialize the weight matrices of the neural 
        network with optional bias nodes"""
        
        bias_node = 1 if self.bias else 0
        
        rad = 1 / np.sqrt(self.no_of_in_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes + bias_node))

        rad = 1 / np.sqrt(self.no_of_hidden_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes + bias_node))
        
        
    def cubeToData(self, c):
        data = []
        for cubie in c.allPieces:
            if c.isCorrectOrientation(cubie):
                data.append(1)
            else:
                data.append(0)
        return data

    def train(self, c):
        input_vector = self.cubeToData(c)
        
        # input_vector and target_vector can be tuple, list or ndarray
        bias_node = 1 if self.bias else 0
        if self.bias:
            # adding bias node to the end of the inpuy_vector
            input_vector = np.concatenate( (input_vector, [self.bias]) )
                                    
        input_vector = np.array(input_vector, ndmin=2).T                    

        output_vector1 = np.dot(self.weights_in_hidden, input_vector)
        output_vector_hidden = activation_function(output_vector1)
        
        if self.bias:
            output_vector_hidden = np.concatenate( (output_vector_hidden, [[self.bias]]))
        
        
        output_vector2 = np.dot(self.weights_hidden_out, output_vector_hidden)

        largestInd = -1
        largestVal = -1
        for i in range(len(output_vector2)):
            if self.lastMove != i and largestVal < output_vector2[i]:
                largestInd = i
                largestVal = output_vector2[i]
        
        if largestInd == 0:
            c.rotateF(True)
        elif largestInd  == 1:
            c.rotateF(False)
        elif largestInd  == 2:
            c.rotateB(True)
        elif largestInd  == 3:
            c.rotateB(False)
        elif largestInd  == 4:
            c.rotateL(True)
        elif largestInd  == 5:
            c.rotateL(False)
        elif largestInd  == 6:
            c.rotateD(True)
        elif largestInd  == 7:
            c.rotateD(False)
        elif largestInd  == 8:
            c.rotateU(True)
        elif largestInd  == 9:
            c.rotateU(False)
        elif largestInd  == 10:
            c.rotateR(True)
        elif largestInd  == 11:
            c.rotateR(False)
            
        self.lastMove = largestInd
        #print(largestInd)

        outputVec = np.array(self.cubeToData(c), ndmin=2).T
        output_vector3 = np.dot(self.weights_in_hidden, outputVec)
        output_vector_hidden = activation_function(output_vector3)
        output_vector4 = np.dot(self.weights_hidden_out, output_vector_hidden)
        
        output_vector_network = activation_function(output_vector4)
        output_errors = np.array([1 for i in range(12)], ndmin=2).T - output_vector_network
        output_errors[largestInd][0] *= 0.5
        
        # update the weights:
        tmp = output_errors * output_vector_network * (1.0 - output_vector_network)
        #print(tmp)
        #print(np.dot(tmp, output_vector_hidden.T))
        tmp = self.learning_rate  * np.dot(tmp, output_vector_hidden.T)
        
        #print(tmp)
        #print(self.weights_hidden_out)
        self.weights_hidden_out += tmp
        #print(self.weights_hidden_out)

        # calculate hidden errors:
        hidden_errors = np.dot(self.weights_hidden_out.T, output_errors)
        # update the weights:
        tmp = hidden_errors * output_vector_hidden * (1.0 - output_vector_hidden)
        if self.bias:
            x = np.dot(tmp, input_vector.T)[:-1,:]     # ???? last element cut off, ???
        else:
            x = np.dot(tmp, input_vector.T)
        self.weights_in_hidden += self.learning_rate * x
        
       
    
    def run(self, c):
        # input_vector can be tuple, list or ndarray
        input_vector = self.cubeToData(c)
        
        if self.bias:
            # adding bias node to the end of the inpuy_vector
            input_vector = np.concatenate( (input_vector, [1]) )
        input_vector = np.array(input_vector, ndmin=2).T

        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        
        if self.bias:
            output_vector = np.concatenate( (output_vector, [[1]]) )
            

        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)
    
        return output_vector
            
'''
class1 = [(3, 4), (4.2, 5.3), (4, 3), (6, 5), (4, 6), (3.7, 5.8),
          (3.2, 4.6), (5.2, 5.9), (5, 4), (7, 4), (3, 7), (4.3, 4.3) ] 
class2 = [(-3, -4), (-2, -3.5), (-1, -6), (-3, -4.3), (-4, -5.6), 
          (-3.2, -4.8), (-2.3, -4.3), (-2.7, -2.6), (-1.5, -3.6), 
          (-3.6, -5.6), (-4.5, -4.6), (-3.7, -5.8) ]

labeled_data = []
for el in class1:
    labeled_data.append( [el, [1, 0]])
for el in class2:
    labeled_data.append([el, [0, 1]])
  

np.random.shuffle(labeled_data)
print(labeled_data[:10])

data, labels = zip(*labeled_data)
labels = np.array(labels)
data = np.array(data)
'''
 
c = convert(readColors())
nn = NeuralNetwork(27, 12, 27, 0.1)
for i in range(10000):
    nn.train(c)
    output = nn.run(c)
    print(nn.cubeToData(c))
