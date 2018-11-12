#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 2: MNIST Example with annotation
# Created 11/6/2018

# Version 0.1
# No updates yet...
# No changes to report!

# Planned features / updates:
#   o Find way to cleanly and succinctly put modules in keras datasets into
#       a set (for ease of training on different data).

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import textwrap
from math import *
import tensorflow as tf
import matplotlib.pyplot as ppt
import numpy as np

# Temporary import, as deepcopy is slow
from copy import deepcopy

# Print keras datasets for learning purposes
dataSets = set()
for dat in dir(tf.keras.datasets):
    if dat[0] != "_":
        dataSets.add(dat)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

# Simple (?) function to tranform elements of a square matrix given a lambda
#expression used to modify them.
def transformElems(matrix, lamb):
    matCopy = deepcopy(matrix)
    return list(map(lambda row: list(map(lambda x: lamb(x), row)), matCopy))

# Simple way to show an image corresponding to a slice of
#a given tensor dataset. Optionally transform data by setting optional
#param tForm to True.
def showDataRep(data, index, tForm = False, lamb = lambda x: x):
    if tForm:
        ppt.imshow(transformElems(data[index], lamb))
    else:
        ppt.imshow(data[index])
    ppt.show()

# Simplifies keras normalize call.
def normData(data, axis = 1):
    return tf.keras.utils.normalize(data, axis)

# Adds layers iteratively, defaulting to a rectified linear unit activation
#with densely connected layers.
def addLayers(model, numLayers, nodes, act = tf.nn.relu):
    for i in range(numLayers):
        model.add(tf.keras.layers.Dense(nodes, activation = act))

                #==========================================#
            #~~~~~~~~~~~~] Exp 1: Visual Transform [~~~~~~~~~~~~#
                #==========================================#

# Preps the training data and norms it for our model
trainDat = tf.keras.datasets.mnist
(xTrain, yTrain), (xTest, yTest) = trainDat.load_data()
xTrain, xTest = normData(xTrain), normData(xTest)

# Tests to ensure that everything is working fine.
showDataRep(xTrain, 1)
showDataRep(xTrain, 1, tForm = True, lamb = lambda x: 50 * (x % 2))



                #==========================================#
            #~~~~~~~~~~~~]   Exp 2: TF Neural Net  [~~~~~~~~~~~~#
                #==========================================#

# First, we construct our model. Because this is just a simple neural network
#without convolutions, we will want to flatten our list before doing anything.

modelA = tf.keras.models.Sequential()



# As mentioned previously, we want to flatten any input data, so we make sure
#layer 1 is a flattening layer.

modelA.add(tf.keras.layers.Flatten())
addLayers(modelA, 5, 128)



# Final layer is simply the digit determining layer, and so we want a
#probability based activation and not the relu.

addLayers(modelA, 1, 10, act = tf.nn.softmax)
modelA.compile(optimizer = 'adam',
               loss = 'sparse_categorical_crossentropy',
               metrics = ['accuracy'])



# Now, we train our model. I had some time, so I did a lot of epochs.
modelA.fit(xTrain, yTrain, epochs = 3)



# Now for fun, we test the model on the dataset AND a tranformed set.
(loss1, acc1) = modelA.evaluate(xTrain, yTrain)
print("Loss 1: " + str(loss1), "\nAccuracy 1: " + str(acc1))



# Finally, we demonstrate that we've actually made a neural network.
predictions = modelA.predict([xTest])
for i in range(200):
    print("The Neural Network predicts that index %d is " % i + \
          str(np.argmax(predictions[i])))
    showDataRep(xTest, i)
