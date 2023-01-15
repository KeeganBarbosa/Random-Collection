# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:33:45 2023

@author: Owner
"""

import numpy as np

def powers(A,k,y):
    if k==0:
        return(y)
    else:
        for i in range(1,k+1):
            y= np.dot(A,y)
        return(y)

"""The below only makes sense for adjacency matrices."""

def distance(A,i,j):
    B=A
    d=0
    if i==j:
        return(d)
    else:
        N= A.shape[0]
        e=np.eye(1,N,i)
        for k in range(1,N+1):
            d+=1
            e=np.dot(B,e)
            if e[j]>0:
                return(d)
        else:
            return("vertices are in different connected components.")    
        