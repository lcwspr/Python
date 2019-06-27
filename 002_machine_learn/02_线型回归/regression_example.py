# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:24:08 2019

@author: dell
"""

import numpy as np
import operator

xMat=np.mat('1 1.1 2.1; 1 1.9 3.1; 1 3.1 4')
yMat=np.mat('1.1 2.1 2.9')

xTx=xMat.T*xMat
if np.linalg.det(xTx)==0.0:
    print("This matrix is singular, cannot do inverse")

theta=xTx.I*(xMat.T*yMat.T)

print(theta)