# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:40:20 2023

@author: Owner
"""

import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])

row_ind, col_ind = linear_sum_assignment(cost)

print(cost[row_ind,col_ind].sum())