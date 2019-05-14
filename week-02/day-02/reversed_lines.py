# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    file = open(file_name,"r+")
    decode_file = open("C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\dereversed.txt","w+")
    for line in file.readlines():
        decode_file.write(line[::-1])
    file.close()
    decode_file.close()

filename = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\reverse_line.txt"
decrypt(filename)