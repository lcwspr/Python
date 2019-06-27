# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:51:24 2019

@author: yrchen
"""

import kMeans

import numpy

import matplotlib
import matplotlib.pyplot as plt

dataMat = numpy.mat(kMeans.loadDataSet('testSet.txt'))

myCentroids, clustAssing = kMeans.kMeans(dataMat, 4)
print(myCentroids, clustAssing)

fig = plt.figure()
ax = fig.add_subplot(221)
ax.plot(dataMat[:, 0], dataMat[:, 1], 'go')

bx = fig.add_subplot(221)
bx.plot(dataMat[:, 0], dataMat[:, 1], 'ro')
plt.show()
print(ax)
