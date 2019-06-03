def squared_above_20(lst):
    return list(filter(lambda x:x**2 > 20,lst))


test_cases = [x for x in range(10)]

print(squared_above_20(test_cases))