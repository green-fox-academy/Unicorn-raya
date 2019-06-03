def my_map(rule,iter_type):
    result = []
    for i in iter_type:
        result.append(rule(i))
    return result

test_cases1 = [1,2,3,4,5,6,7,8,9,10]
test_cases2 = (1,2,3,4,5,6,7,8,9,10)
#test_cases1 = [1,2,3,4,5,6,7,8,9,10]

def double_times(number):
    return 2 * number


print(" ".join(str(i) for i in my_map(double_times,test_cases1)))

print(" ".join(str(i) for i in my_map(double_times,test_cases2)))






