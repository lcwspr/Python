# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import operator

dataSet=np.array([[0,0],[0.1,0],[1,1],[1.1,1]]);
dataLabels=['A','A','B','B'];

newInput=[0.1,0.2]

k=3

dataSetSize=dataSet.shape[0]
diffMat=np.tile(newInput,(dataSetSize,1))-dataSet
sqDiffMat=diffMat**2
sqDistances=sqDiffMat.sum(axis=1)
distances=sqDistances**0.5
sortedDistIndicies=distances.argsort()

classCount={}

for i in range(k):
    voteIlabel=dataLabels[sortedDistIndicies[i]]
    classCount[voteIlabel]=classCount.get(voteIlabel,0)+1

sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

classifyResult=sortedClassCount[0][0]

print(classifyResult)