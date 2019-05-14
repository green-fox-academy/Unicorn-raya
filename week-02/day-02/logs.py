# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.

file_name ="C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\log.txt"

#return the list of address that store addresss only show once 
def find_unique_address(filename):
    address = {}
    unique_address = []
    file = open(filename,"r+")
    for line in file.readlines():
        tmp_address = list(line.split())[5]
        if tmp_address in address.keys():
            address[tmp_address] += 1
        else:
            address[tmp_address] = 1
    file.close()
    for key in address.keys():
        if address[key] == 1:
            unique_address.append(key)
    return unique_address

def get_ratio_of_getpost(filename):
    get = 0
    post = 0
    file = open(filename,"r+")
    for line in file.readlines():
        key_word = list(line.split())[6]
        if key_word == "GET":
            get += 1
        elif key_word == "POST":
            post += 1
        else:
            pass
    file.close()
    return (get/post)    

print(find_unique_address(file_name))
print(get_ratio_of_getpost(file_name))

