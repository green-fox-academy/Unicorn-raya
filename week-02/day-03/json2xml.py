import json

json_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\flower.json"
xml_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\flower.xml"

def json2xml(json_file,xml_file):
    pass
    fr=open(json_file,"r")  
    ls=json.load(fr)  
    data=[ list(ls[0].keys()) ]  
    for item in ls:
        data.append(list(item.values()))  
    fr.close()  

    fw=open(xml_file,"w+")  
    for line in data:
        fw.write(",".join(line)+"\n")  #以逗号分隔一行的每个元素，最后换行
    fw.close()  #关闭csv文件
