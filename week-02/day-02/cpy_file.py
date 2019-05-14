# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def cpy_file(orginal_file,cpy_file):
    try:
        count = 0
        file = open(orginal_file,'r')
        cpy = open(cpy_file,'w+')
        for line in file:
            cpy.write(line)
        file.close()
        return count
    except IOError:
        print('cannot open',orginal_file)

cpy_file("my-file.txt","test_cpy.txt")