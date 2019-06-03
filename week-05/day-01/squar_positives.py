def sqrt_positive(lst):
    return list(map(lambda x: x**2,list(filter(lambda x: x > 0 ,lst))))


test_case = [1,2,-3,4,-5,6]

print(sqrt_positive(test_case))