#!/usr/bin/env python
# coding: utf-8

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
import numpy as np
import math
import pandas as pd

def LinearReg(train_data,user_data):
    X = train_data.iloc[0:,1:]
    y = train_data.prices
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    model = LinearRegression()
    model.fit(X,y)
    y_pred = model.predict(X_test)
    #print("MSE:",metrics.mean_squared_error(y_test, y_pred))
    #print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    return model.predict(pd.DataFrame(user_data))

def LinearRegRidge(train_data,user_data):
    X = train_data.iloc[0:,1:]
    y = train_data.prices
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    clf = linear_model.Ridge(alpha = 5).fit(X_train,y_train)
    clf.fit(X_train,y_train)
    r2_score = clf.score(X_test,y_test)
    cv_score = cross_val_score(clf,X_train,y_train,cv = 5)
    y_pred = clf.predict(X_test)
    return clf.predict(pd.DataFrame(user_data))


def AdaboostPd(train_data,user_data):
    X = train_data.iloc[0:,1:]
    y = train_data.prices
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    regressor=AdaBoostRegressor()
    regressor.fit(X_train,y_train)
    pred_y = regressor.predict(X_test)
    mse = mean_squared_error(y_test, pred_y)
    # print(" result: ", pred_y)
    # print(" mse = ",round(mse,2))
    return regressor.predict(pd.DataFrame(user_data))


train_data = pd.read_csv("clean_data.csv")
