# test  fiz-b
def fiz_b(number):
    i = 1
    while i < number:
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz" 
        if i % 3 == 0:
            yield "Fizz"
        if i % 5 == 0:
            yield "Buzz"
        yield i
        i += 1
    return "done"

a = fiz_b(7)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
