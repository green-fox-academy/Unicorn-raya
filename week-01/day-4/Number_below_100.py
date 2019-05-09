import re
r = re.compile(r'\d{1,2}$|100$')
a = "95"
b= "100"
c ="11"
d ="0"
e = "1"
f = "122"

print(re.match(r,a))
print(re.match(r,b))
print(re.match(r,c))
print(re.match(r,d))
print(re.match(r,e))
print(re.match(r,f))