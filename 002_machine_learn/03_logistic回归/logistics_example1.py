# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:22:20 2019
@author: pc
"""
import logistics
from numpy import *
import numpy as np
def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return np.array(dataMat),np.array(labelMat)


    
x,y=loadDataSet()
print (x)
print (y)
theta=logistics.BatGradDescent(x,y)
print (theta)
Weights=logistics.stocGradDescent(x,y,500)
print (Weights)
