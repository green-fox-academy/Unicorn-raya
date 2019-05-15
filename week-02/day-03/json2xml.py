import json

json_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\flower.json"
xml_file = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\flower.xml"

def json2xml(json_file,xml_file):
    pass
    fr=open(json_file,"r")  #打开json文件
    ls=json.load(fr)  #将json格式的字符串转换成python的数据类型，解码过程
    data=[ list(ls[0].keys()) ]  #获取列名,即key
    for item in ls:
        data.append(list(item.values()))  #获取每一行的值value
    fr.close()  #关闭json文件

    fw=open(xml_file,"w+")  #打开csv为文件
    for line in data:
        fw.write(",".join(line)+"\n")  #以逗号分隔一行的每个元素，最后换行
    fw.close()  #关闭csv文件
