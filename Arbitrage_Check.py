# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def Arbitrage_Opportunity(Weights,n):
    P =[[ [ 0 for i in range(n) ] for j in range(n) ] for m in range(n+1)]
    for i in range(n):
        for j in range(n):
            P[0][i][j] = Weights[i][j]
    for m in range(n):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    P[m+1][i][k] = max(P[m][i][j]*Weights[j][k],P[m][i][k])
                    if P[m+1][i][k]*Weights[k][i]>1:
                        return("arbitrage found", P[m+1][i][k]*Weights[k][i])
    return("no arbitrage found")


Sample =[[1,1.1586,1.6939],[1/1.1586,1,1.46],[1/1.6939,1/1.46,1]]

print(Arbitrage_Opportunity(Sample,len(Sample)))
