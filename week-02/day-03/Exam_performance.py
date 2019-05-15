import re
import pandas as pd

def format2seconds(time_string):
    hour = 0
    minutes = 0
    seconds = 0    
    if re.compile(r'([\d]+)s').match(time_string):
        seconds += float(re.compile(r'([\d]+)s').match(time_string).group(1))

    if re.compile(r'([\d]+)m').match(time_string):
        minutes += float(re.compile(r'([\d]+)m').match(time_string).group(1))    

    if re.compile(r'(.[\d]+)h').match(time_string):
        #print("ummmmm")
        hour += float(re.compile(r'(.[\d]+)h').match(time_string).group(1))

    if re.compile(r'([\d]+)h([\d]+)m([\d]+)s').match(time_string):
        #print("ummmmm")
        hour += float(re.compile(r'([\d]+)h([\d]+)m([\d]+)s').match(time_string).group(1))
        minutes += float(re.compile(r'([\d]+)h([\d]+)m([\d]+)s').match(time_string).group(2))
        seconds += float(re.compile(r'([\d]+)h([\d]+)m([\d]+)s').match(time_string).group(3))
    if re.compile(r"([\d]+):([\d]+):([\d]+)").match(time_string):
        #print('ummmmmm')
        hour += float(re.compile(r"([\d]+):([\d]+):([\d]+)").match(time_string).group(1))
        minutes += float(re.compile(r"([\d]+):([\d]+):([\d]+)").match(time_string).group(2))
        seconds += float(re.compile(r"([\d]+):([\d]+):([\d]+)").match(time_string).group(3))
    if time_string == "null":
        return 0 

    return (hour*60 + minutes)*60 + seconds
        
# test_cases = ["3600s","1h2m20s","600s","32m",".5h","1h12m38s","65m","98s","1:02:08"]
# print(format2seconds(test_cases[8]))

def get_tsv_file(tsv_file_name):
    data_in_list = []
    with open(tsv_file_name) as tsv_file:
        buffer = tsv_file.readlines()
        for index in range(1,len(buffer)):
            data_in_list.append(buffer[index])
    max_number = -1
    point = 0
    min_number = 999999
    #print(data_in_list)
    for line in data_in_list:
        tmp_number = format2seconds(list(line.split('\t'))[2])
        #print(tmp_number)
        if tmp_number > max_number:
            max_number = tmp_number
            point = int(list(line.split('\t'))[1])
        if tmp_number < min_number and tmp_number != 0:
            min_number = tmp_number

    #return point,max_number
    return point/max_number

tsv_file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\exams.tsv"

print(get_tsv_file(tsv_file_name))
