def avg_even_number(lst):
    l =list(filter(lambda x:x%2 ==1,lst))
    if len(l) != 0:
        return sum(l)/len(l)
    else:
        return "ops~"


test_cases = [x for x in range(5) if x%2 == 1 ]
test_cases_2 = [x for x in range(5) if x%2 == 0 ]
test_cases_3 = [x for x in range(5)]


print(avg_even_number(test_cases))

print(avg_even_number(test_cases_2))

print(avg_even_number(test_cases_3))