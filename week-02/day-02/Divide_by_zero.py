# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

def divide(vars):
    try:
        number = 10/vars
        return number
    except ZeroDivisionError:
        print("cannot divide zero!")
    

print(divide(2))

print(divide(0))


