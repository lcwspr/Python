# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:01:43 2019

@author: dell
"""
import numpy as np
import operator

def algorithmKNN(dataSet, dataLabels,k,newInput):

    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(newInput,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    # argsort函数是对一维数组进行排序，返回排序后的索引
    classCount={}
    #classCount是一个字典，例：classCount={'A':3,'B':2,'C':5}
    for i in range(k):
        voteIlabel=dataLabels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        #用get函数获得当前制定值下的计算值
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    # iteritems将字典中所有项，以迭代器方式返回。例，classCount.iteritems()=[('A',3),('B',2),('C',5)]
    # key=operator.itemgetter(1): 根据第二个阈值进行排序。例：根据3,2,5的值进行排序
    return sortedClassCount[0][0]