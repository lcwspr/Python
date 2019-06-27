# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:46:50 2019

@author: dell
"""

import numpy as np
import operator


def algorithmRegression(xMat,yMat):
    xTx=xMat.T*xMat
    if np.linalg.det(xTx)==0.0:
        print("This matrix is singular, cannot do inverse")
    ws=xTx.I*(xMat.T*yMat)
    return ws