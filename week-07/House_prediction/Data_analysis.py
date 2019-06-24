#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from pandas import Series,DataFrame
from pandas import to_datetime
import math

postcode_path = "postcodes.csv"
house_path = "Somerset.csv"
postcode = pd.read_csv(postcode_path,usecols=['postcode', 'Latitude', 'Longitude','Distance To Station (KM)'])
house = pd.read_csv(house_path)
#cities.drop(cities.columns[0],axis=1,inplace=True) # drop 1st columns
#postcode
house
postcode = postcode.rename(columns={'Distance To Station (KM)': 'path2station'})

# info = "TA8 1EW"
# post_info = postcode[(postcode["Postcode"] == info) & (postcode["In Use?"] == "Yes")]
# postcode["new test"] = postcode["Longitude"]
data = pd.merge(house,postcode,how = 'left',left_on='postcode',right_on="postcode")
data.to_csv("raw_data.csv")
#data

data = data[ data['Latitude'].isnull() == False ]#drop info without (x,y)
data.drop(columns = ['postcode'],inplace=True)
data.drop(columns = ['city'],inplace=True)
data = data.fillna(int(math.ceil(data['noBed'].mean())))
import math
data['prices'] = data['prices'].apply(math.log)
def plusone(num):
    return num + 1

def housetype2num(housetype):
    if housetype == "Semi-Detached":
        return 1
    elif housetype == "Detached":
        return 2
    elif housetype == "Terraced":
        return 3
    elif housetype == "Flat":
        return 4
    else:
        return 0

data['ownership'] = data['ownership'].apply(plusone)
data['new'] = data['new'].apply(plusone) 
data['house_types'] = data['house_types'].apply(housetype2num)

data['date'] = pd.to_datetime(data['date'])
data = data[data['date'] > '2015-01-01']
data.drop(columns = ['date'],inplace=True)
data = pd.get_dummies(data)
data.to_csv("clean_data.csv",index = None)

