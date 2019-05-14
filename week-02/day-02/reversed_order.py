# Create a method that decrypts reversed-order.txt
def decrypt(file_name):
    file = open(file_name,"r+")
    decode_file = open("C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\deordered.txt","w+")
    cache = file.readlines()
    for index in range(len(cache)):
        decode_file.write(cache[len(cache) - index - 1])
    file.close()
    decode_file.close()

file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-02\\reversed_order_file.txt"
decrypt(file_name)