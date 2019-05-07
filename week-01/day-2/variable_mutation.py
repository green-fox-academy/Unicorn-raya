a = 3
# make the "a" variable's value bigger by 10
a += 10
print(a)

b = 100
# make b smaller by 7
b -= 7
print(b)

c = 44
# please double c's value
c *= 2
print(c)

d = 125
# please divide by 5 d's value
d /= 5
print(d)

e = 8
# please cube of e's value
e **= 3
print(e)

f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
if f1 > f2:
    print("f1 is bigger than f2")
else:
    print("Nope~")

g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)

if 2 * g2 > g1:
    print( "double of g2 is bigger than g1 " )
else:
    print("Nope~ for g2")

h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)

if h % 11 == 0:
    print("11 is a divisor of h")
else:
    print("Nope~")

i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

if i1 > i2**2 and i1 < i2**3:
    print(" i1 is larger than i2^2 and less than i2^3 ")
else:
    print("Nope~")

j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)

if j % 3 == 0 or j % 5 ==0:
    print("j is divsiable by 3 or 5")
else:
    print("Nope~ ")

#print(k)