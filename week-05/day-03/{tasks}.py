def number_adder(number):
    if number == 1 or number == 0:
        return number
    else:
        return number + number_adder(number - 1)

def sum_digits(number):
    if number % 10 == 0:
        return number 
    else:
        return number % 10 + sum_digits(number // 10)

def my_power(number,times):
    if times == 1:
        return number
    else:
        return number * my_power(number,times - 1)

def gcd(number1, number2):
    if number2 != 0:
        return gcd(number2, number1 % number2)
    else:
        return number1
def bunnies(number):
    if number == 1:
        return 2
    else:
        return 2 + bunnies(number - 1)

def bunnies_advanced(number):
    if number == 1:
        return 2
    else:
        if number % 2 == 0:
            return 3 + bunnies_advanced(number - 1)
        else:
            return 2 + bunnies_advanced(number - 1)

def change_string(sample_string,index=0,new_string = ""):
    if index != len(sample_string):
        if sample_string[index] == 'x':
            new_string += 'y'
        else:
            new_string += sample_string[index]       
        return change_string(sample_string,index+1,new_string)
    else:
        return new_string

def change_string_2(sample_string,index=0,new_string = ""):
    if index != len(sample_string):
        if sample_string[index] != 'x':
            new_string += sample_string[index]       
        return change_string_2(sample_string,index+1,new_string)
    else:
        return new_string

def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

def max_finder(number_list,index = 0,tmp_max = -999999):
    if index != len(number_list):
        if number_list[index] > tmp_max:
            tmp_max = number_list[index]
        return max_finder(number_list,index + 1, tmp_max)
    else:
        return tmp_max
