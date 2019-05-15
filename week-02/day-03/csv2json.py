csv_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\user.csv"
json_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\user.json"
import json
def csv2json(csv_file,json_file):
    fo=open(csv_file,"r+") 
    ls=[]
    for line in fo:
        line=line.replace("\n","") 
        ls.append(line.split(",")) 
    fo.close()  
    fw=open(json_file,"w")  
    for i in range(1,len(ls)):  
        ls[i]=dict(zip(ls[0],ls[i]))  
    
    json.dump(ls[1:],fw,sort_keys=True,indent=4)
    fw.close()

csv2json(csv_file,json_file)