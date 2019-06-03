def get_even(lst):
    return list(filter(lambda x: x%2 == 1,lst))

test_case = [x for x in range(10)]

print(get_even(test_case))

