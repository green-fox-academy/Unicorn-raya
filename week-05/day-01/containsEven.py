def all_positive(lst):
    return len(list(filter(lambda x: x%2 == 1,lst))) == 0


test_cases = [x * 2 for x in range(5)]

test_cases_2 = [1, 3, 2, 4, 7, 3, 8, 12, 19, 6, 9, 10, 14]


print(all_positive(test_cases))

print(all_positive(test_cases_2))