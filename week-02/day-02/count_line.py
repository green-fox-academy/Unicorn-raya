# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines_in_files(filename):
    try:
        count = 0
        file = open(filename,'r')
        for line in file:
            count +=1
        file.close()
        return count
    except IOError:
        print('cannot open',filename)

print(count_lines_in_files("C:/Users/Ray_Zhang/greenfox/Unicorn-raya/week-02/day-02/aaa.txt"))
count_lines_in_files("asdasasdsa")
