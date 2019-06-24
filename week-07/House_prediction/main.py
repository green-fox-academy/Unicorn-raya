from flask import Flask, request, render_template, jsonify, make_response, json
import pandas as pd
from model_sim import LinearReg,LinearRegRidge,AdaboostPd
import numpy as np
import folium

app = Flask(__name__)

@app.route("/")
def Navigation():
    return render_template("Home.html")

@app.route('/analysis',methods=['get'])
def saveTrainAttr():
    Postcode = request.args.get('postcode')
    noBed  = request.args.get('noBed')
    ownership = request.args.get('ownership')
    path2station = request.args.get('path2station')
    house_types = request.args.get('house_types')
    new_house = request.args.get('new_house')
    user_info = [house_types,ownership,new_house,noBed,Postcode,path2station]
    data_info = []
    data_info.append(houstType2num(house_types))
    data_info.append(ownership2number(ownership))
    data_info.append(newbuild2bin(new_house))
    data_info.append(noBed)
    coor = post2Cor(Postcode)
    data_info.extend(coor)
    data_info.append(path2station)
    number_1 = int(LinearReg(pd.read_csv("clean_data.csv"),[data_info]))
    number_2 = int(LinearRegRidge(pd.read_csv("clean_data.csv"),[data_info]))
    number_3 = int(AdaboostPd(pd.read_csv("clean_data.csv"),[data_info]))
    number = max(number_1,number_2,number_3)
    surround = getSurroundCoor(coor)
    getResultPages(coor,number,surround) 
    return render_template('result.html',result = number, input_data = user_info)

def getSurroundCoor(target_cor,csv_file = "clean_data.csv"):
    data = pd.read_csv(csv_file)
    r = 0.005
    data = data[ (data["Latitude"] < target_cor[0]+ r) & (data["Latitude"] > target_cor[0]-r)]
    data = data[ (data["Longitude"] < target_cor[1]+ r) & (data["Longitude"] > target_cor[1]-r)]
    data = data[['prices','Latitude','Longitude']]
    prices = np.array(data['prices']).astype(np.str).tolist()
    cors = np.array(data[['Latitude','Longitude']]).astype(np.str).tolist()
    return [prices,cors]

#show up target_cor in cloud iron and surround_cors in blue circle
#para surround_cor[0] is the prices and [1] is corrdinators
def getResultPages(target_cor,target_value,surround_cor):
    oneUserMap = folium.Map(location=target_cor,zoom_start=15,disable_3d = False)
    for e,f in zip(surround_cor[1],surround_cor[0]):
        folium.Marker(
        [e[0],e[1]],
        icon=folium.Icon(color='blue', icon='info-sign'),
        popup=f'Sold price here is ₤{f}',
        ).add_to(oneUserMap)
    folium.Marker(
        target_cor,
        icon=folium.Icon(color='red', icon='cloud'),
        popup=f'Estimate price is ₤{target_value}',
        number_of_sides=8,
        ).add_to(oneUserMap)    
    oneUserMap.save('templates/result.html')
#getResultPages(target,'10000000',surround)

#turn house type to numbers ->[1,2,3,4]
def houstType2num(house_type):
    if house_type == "Semi-Detached":
        return 1
    elif house_type == "Detached":
        return 2
    elif house_type == "Terraced":
        return 3
    elif house_type =="Flat":
        return 4
    else:
        return 0

#ownership -> (1,2)
def ownership2number(ownership):
    if ownership == "Freehold":
        return 1
    elif ownership == "Leasehold":
        return 2
    else:
        return 0
#new -> 2, old -> 1
def newbuild2bin(newHouse):
    if newHouse =="Yes":
        return 2
    elif newHouse == "No":
        return 1
    else:
        return 0

#postcode -> latitude and longitude
def post2Cor(postcode):
    postfile = "static\postcodes.csv"
    data = pd.read_csv(postfile)
    search_list = data[ data['postcode'] == postcode]
    if len(search_list) != 0:
        return [float(search_list.Latitude),float(search_list.Longitude)]
    else:
        return ["Invalid Postcode"]

if __name__ == "__main__":
    app.run(debug = True,use_reloader = True)

