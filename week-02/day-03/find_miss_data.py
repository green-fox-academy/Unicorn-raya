import csv

def find_missing_data(filename):
    file = open(filename, "r")
    csv_file = csv.reader(file)
    format_file = open("C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\format_data.txt","w+")
    for line in csv_file:
        if "" in line or len(line) < 4:
            print(line)
        else:
            format_file.write(" ".join(line)+'\n')
    
    file.close()
    format_file.close()

filename = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\missdata.csv"
find_missing_data(filename)
   