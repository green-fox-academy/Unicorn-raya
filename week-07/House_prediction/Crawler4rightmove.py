#!/usr/bin/env python
# coding: utf-8

import requests
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from pandas import Series,DataFrame
from pandas import to_datetime
from bs4 import BeautifulSoup

total_pages = 40
num_in_page = 25
addresses = []
prices = []
house_types=[]
ownerships=[]
builds = []
dates=[]
noBeds = []
city = []

ownership_dic = {" Freehold":0," Leasehold":1}
resi_dic = {" Residential":0," Residential\xa0(New Build)":1}

cities = {'Bath':'116','Bridgwater':'212','Burnham-On-Sea':'251','Chard':'301','Cheddar':'306','Clevedon':'337','Crewkerne':'381','Frome':'536','Glastonbury':'551','Ilminster':'678','Minehead':'942','Radstock':'1109','Shepton+Mallet':'1198','Street':'1287','Taunton':'1317','Wellington':'1414','Wells':'1415','Weston-Super-Mare':'1437','Wincanton':'1458','Yeovil':'1497'}
for key,value in cities.items():
    print(key)
    for index in range(0,total_pages * num_in_page,num_in_page):
        print(index)
        baseUrl = f"https://www.rightmove.co.uk/house-prices/detail.html?country=england&locationIdentifier=REGION%5E{value}&searchLocation={key}&index="
        page = requests.get(baseUrl + str(index))
        soup = BeautifulSoup(page.content,'html.parser')
        #soup.prettify()
        house_data = soup.find_all('div',{"class":"soldDetails"})
        soldAddress = soup.find_all(['a','div'],{'class':'soldAddress'})
        soldPrice = soup.find_all('td',{'class':'soldPrice'})
        soldDate = soup.find_all('td',{'class':'soldDate'})
        soldNoBed = soup.find_all('td',{'class':'noBed'})
        soldType = soup.find_all('td',{'class':'soldType'})
        housetype = soldType[0] 
        ownership = soldType[1]
        build = soldType[2]
        
        for i in range(num_in_page):
            addresses.append(" ".join(soldAddress[i].text.split(' ')[-2:]))
            price = soldPrice[i].text
            prices.append(price.strip('£').replace(',',""))
            house_types.append(soldType[i].text.split(',')[0])
            ownerships.append(ownership_dic[soldType[i].text.split(',')[1]])
            builds.append(resi_dic[soldType[i].text.split(',')[2]])
            dates.append(soldDate[i].text)
            noBeds.append(soldNoBed[i].text.split(" ")[0])
            city.append(key)

data_dic = {'postcode':addresses,'prices':prices,'house_types':house_types,'ownership':ownerships,'new':builds,'date':dates,'noBed':noBeds,'city':city} 
tmp_data = pd.DataFrame(data_dic)
tmp_data.to_csv('Somerset.csv',index = None)

print('done') 
