import csv 
file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\movie.csv"

def find_oldest_movie(filename):
    year = 99999999
    title = ""
    director = ""
    file = open(filename, "r")
    csv_file = csv.reader(file)
    for line in csv_file:
        tmp_year = int(list(line[0].split(";"))[1])
        #print(tmp_year)
        if year > tmp_year:
             year = tmp_year
             director = list(line[0].split(";"))[2] 
             title = list(line[0].split())[0]
    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"director: {director}")
    
find_oldest_movie(file_name)
