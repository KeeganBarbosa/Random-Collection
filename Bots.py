# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:26:04 2023

@author: Owner
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('activity_botscore.csv')
data=data.rename(columns={'bot_score_english':'bot_score'})

correlation = data.corr()

plt.figure(figsize=(10,8))
sns.heatmap(correlation,annot=True,
            cmap=sns.color_palette("mako"),
            linewidth=2,edgecolor="k")
plt.title("Correlation Matrix")

"""Activity and count unsurprisingly correlated, so drop count as it is less vital."""

data=data.drop(['count'],axis='columns')

data.plot.scatter(y='bot_score',x='activity')

linear_regressor = LinearRegression()

X = data.iloc[:, 2].values.reshape(-1, 1)

Y = data.iloc[:, 3].values.reshape(-1, 1)


linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)


Y_pred = linear_regressor.predict(X)



plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()

print("Coeff %.9f" % linear_regressor.coef_)

print("Intercet %.9f" % linear_regressor.intercept_)

print("Mean Squared error %.9f" % mean_squared_error(Y,Y_pred))

print("R_2 %.9f" % r2_score(Y, Y_pred))

"Linear clearly is not good fit, which is apparent from image."


print(data[data['bot_score']>0.95 ].count())

binary_data = data


binary_data['bot_score'].values[binary_data['bot_score'] > 0.95] = 1

binary_data['bot_score'].values[binary_data['bot_score'] <= 0.95] = 0

binary_correlation = binary_data.corr()

plt.figure(figsize=(10,8))
sns.heatmap(correlation,annot=True,
            cmap=sns.color_palette("mako"),
            linewidth=2,edgecolor="k")
plt.title("Binary Correlation Matrix")


binary_data.plot.scatter(y='bot_score',x='activity')



X_bin = binary_data.iloc[:, 2].values.reshape(-1, 1)

Y_bin = binary_data.iloc[:, 3].values.reshape(-1, 1)


linear_regressor = LinearRegression()
linear_regressor.fit(X_bin, Y_bin)

logistic_regressor=LogisticRegression()

logistic_regressor.fit(X_bin, Y_bin)



Y_bin_pred = linear_regressor.predict(X_bin)

logY_bin_pred = logistic_regressor.predict(X_bin)



plt.scatter(X_bin, Y_bin)
plt.plot(X_bin, Y_bin_pred, color='red')
plt.plot(X_bin, logY_bin_pred, color='black')
plt.show()

print("Coeff %.9f" % linear_regressor.coef_)

print("Intercept %.9f" % linear_regressor.intercept_)

print("Mean Squared error %.9f" % mean_squared_error(Y_bin,Y_bin_pred))

print("R_2 %.9f" % r2_score(Y_bin, Y_bin_pred))



print("Logistic Coeff %.9f" % logistic_regressor.coef_)

print("Logistic Intercept %.9f" % logistic_regressor.intercept_)

print("Logistic Mean Squared error %.9f" % mean_squared_error(Y_bin,logY_bin_pred))

print("Logistic R_2 %.9f" % r2_score(Y_bin, logY_bin_pred))


print("Logistic Regressor Score %.9f" % logistic_regressor.score(Y_bin, logY_bin_pred))