def fibo(number):
    n,a,b = 0,0,1
    while n < number:
        yield b
        a, b = b, a + b
        n += 1
    return "done"

f = fibo(7)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
