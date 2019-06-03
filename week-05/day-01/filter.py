def my_filter(rule,iter_type):
    result = []
    for i in iter_type:
        if rule(i):
            result.append(i)
    return result

test_cases1 = [1,2,3,4,5,6,7,8,9,10]
test_cases2 = (1,2,3,4,5,6,7,8,9,10)
#test_cases1 = [1,2,3,4,5,6,7,8,9,10]

def larger_than_three(number):
    return number > 3


print(" ".join(str(i) for i in my_filter(larger_than_three,test_cases1)))

print(" ".join(str(i) for i in my_filter(larger_than_three,test_cases2)))






