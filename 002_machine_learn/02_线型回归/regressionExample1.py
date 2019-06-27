# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:50:57 2019

@author: dell
"""

import numpy as np
import operator
import regression as reg

xMat=np.mat('1 1.1 2.1; 1 1.9 3.1; 1 3.1 4')
yMat=np.mat('1.1 2.1 2.9')

ws=reg.algorithmRegression(xMat,yMat.T)