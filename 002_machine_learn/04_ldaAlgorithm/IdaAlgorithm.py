# -*- coding:utf-8 -*-
'''
    show the IdaAlgorithm
'''

import numpy as np

mydataset = [
    [0.697,0.460,1],[0.774,0.376,1],[0.634,0.264,1],[0.608,0.318,1],
    [0.556,0.215,1],[0.403,0.211,1],[0.481,0.149,1],[0.437,0.211,1],
    [0.666,0.091,0],[0.243,0.267,0],[0.245,0.057,0],[0.343,0.099,0],
    [0.639,0.161,0],[0.657,0.198,0],[0.360,0.370,0],[0.593,0.042,0]]

datasetNew = np.array(mydataset)
data = datasetNew[0:, 0:2]
label = datasetNew[:,-1]

x0 = data[label == 0]
x1 = data[label == 1]

m, n = np.shape(data)

u0 = x0.mean(0).reshape(1, n)
u1 = x1.mean(0).reshape(1, n)

sw = (x1 - u1).T.dot(x1 - u1) + (x0 - u0).T.dot(x0 - u0)
w = (u0 - u1).dot(np.linalg.inv(sw))

print(w)


