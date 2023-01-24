# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:05:16 2023

@author: Owner
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('NFT_Rug_Pulls.csv')

data

data=data.rename(columns={'Date':'date','Company Name':'company',
                          'Crypto vs NFT':'coin_type',
                          'Rug Pull vs Scam':'scam_type',
                          'Amount Stolen':'damage'})


coin_count = data.coin_type.value_counts()


data = data.drop(['company','date'],axis='columns')


"We need a way to compare nonnumeric, so we do one_hot_encoding"

one_hot_data = data



one_hot_data.replace('NFT', 0, inplace=True)

one_hot_data.replace('Crypto', 1, inplace=True)

one_hot_data.replace('Scam', 0, inplace=True)

one_hot_data.replace('Rug Pull', 1, inplace=True)

one_hot_data['damage']=one_hot_data['damage'].str.replace(',','')

one_hot_data['damage']=one_hot_data['damage'].astype(float)

print(one_hot_data.dtypes)

correlation = one_hot_data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation,annot=True,
            cmap=sns.color_palette("mako"),
            linewidth=2,edgecolor="k")
plt.title("Correlation Matrix")
# plt.show()