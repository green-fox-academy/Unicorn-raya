def sum_even_number(lst):
    return sum(list(filter(lambda x:x%2 ==1,lst)))


test_cases = [x for x in range(5) if x%2 == 1 ]
test_cases_2 = [x for x in range(5) if x%2 == 0 ]


print(sum_even_number(test_cases))


print(sum_even_number(test_cases_2))