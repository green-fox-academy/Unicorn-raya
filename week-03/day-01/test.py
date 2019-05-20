def pprint(num):
    if num == 1:
        print(num)
    else:
        pprint(num - 1)

pprint(10)
