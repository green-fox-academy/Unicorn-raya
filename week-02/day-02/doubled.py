# Create a method that decrypts the duplicated-chars.txt

def decrypt(filename):
    file = open(filename,"r+")
    decode_file = open("C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\dedouble.txt","w+")
    for line in file.readlines():
        string = ""
        for i in range(0,len(line),2):
            string += line[i]
        decode_file.write(string)
    file.close()
    decode_file.close()

file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\double.txt"
decrypt(file_name)