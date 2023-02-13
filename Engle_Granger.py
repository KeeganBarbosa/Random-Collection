# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 10:32:50 2023

@author: Owner
"""
import numpy as np

def Regression_On_Column(A,i):
    X=np.delete(A,i,1)
    T=X.transpose()
    y=A[:i]
    Theta=np.linalg.inv((T.dot(X))).dot(T.dot(y))
    Right = X.dot(Theta)-y
    Left = Right.transpose()
    Cost=Left.dot(Right)
    Cost= (1/(2*len(y))).dot(Cost)
    return([Theta,Cost])

"""
We need to do better with the regression function.
As stands, above will only work when inverse exists
and time series has small amount of inputs.
Ought to use gradient descent to find approx min in future. 
"""

"""Run regression against each column, find best column to regress wrt LS, produce cointegrated portfolio."""

def Engle_Granger(A):
    Thetas=[]
    Costs=[]
    for i in range(A.shape[1]):
        ans = Regression_On_Column(A, i)
        Thetas.append(ans[0])
        Costs.append(ans[1])
    Best_Cost=min(Costs)
    index=Best_Cost.index(Costs)
    return([Costs[index],Thetas[index]])
