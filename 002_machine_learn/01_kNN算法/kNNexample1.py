# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:25:08 2019

@author: dell
"""

import numpy as np

import classifyKNN as kNN

def createDataSet( ):
    group =np.array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

myGroup,myLabels=createDataSet()

myInput=[1.1,1.1]

m=3

output=kNN.algorithmKNN(myGroup,myLabels,m,myInput)

print(output)


