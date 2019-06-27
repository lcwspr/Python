# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:42:23 2019
@author: pc
"""
import random
from numpy import *
import logistics

def sigmoid(X):
    return 1.0/(1.0+exp(-X))

def BatGradDescent(x,y):
    xMat=mat(x)
    yMat=mat(y).transpose()
    m,n=shape(xMat)
    alpha=0.001
    maxCycles=500
    theta=ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(xMat*theta)
        error=(h-yMat)
        theta=theta-alpha*xMat.transpose()*error
    return theta

def stocGradDescent(x,y,numIter):
    m,n=shape(x)
    Weights=ones(n)
    for j in range(numIter):
        for i in range(m):
            alpha=0.001
            randIndex=int(random.uniform(0,m))
            h=sigmoid(sum(x[randIndex].dot(Weights)))
            error=h-y[randIndex]
            Weights=Weights-alpha*(error*x[randIndex])
    return Weights

def classifyVector(inX,theta):
    prob=logistics.sigmoid(sum(inX*theta))
    if prob>0.5:return 1.0
    else:return 0.0

