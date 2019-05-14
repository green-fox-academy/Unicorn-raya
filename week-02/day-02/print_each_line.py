# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"

def open_io(filename):
    try:
        file = open(filename,'r')
        for line in file:
            print(line.rstrip())
        file.close()
    except IOError:
        print('cannot open',filename)

open_io("C:/Users/Ray_Zhang/greenfox/Unicorn-raya/week-02/day-02/aaa.txt")
open_io("asdasasdsa")


#absolute path is needed