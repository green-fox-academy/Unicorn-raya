# Hungarian mobile numbers
# Create a regular expression that matches the valid Hungarian mobile numbers.

# Task	Text
# Match	+36 20 473 2746
# Match	+36 30 217 4912
# Match	00 36 70 381 1288
# Match	00 36 31 471 2818
# Skip	+36 20 3173 4717
# Skip	+36 102 237 1121
# Skip	+49 20 483 1273
# Skip	36 70 381 2183

import re
r = re.compile(r"00|\+") #country number 00 or +
r1 = re.compile(r'36') # start from 36
r2 = re.compile(r'[2-9][0-9]')# city number from 20 - 99 
r3 = re.compile(r'\d{3}')# 3 digit, dif size or char will be blocked
r4 = re.compile(r'\d{4}')# 4 digit, 、、、
r5 = re.compile(r'\s')   # match space
real_match_rule = re.compile(r'^(\+|00\s)36\s[2-9][0-9]\s\d{3}\s\d{4}$')
a= " "
b = "     "
c= ""
s1="+36 20 473 2746"
s2="+36 30 217 4912"
s3="00 36 70 381 1288"
s4="00 36 31 471 2818"
s5="+36 20 3173 4717"
s6="+36 102 237 1121"
s7="+49 20 483 1273"
s8="36 70 381 2183"

print(re.match(real_match_rule,s1))
print(re.match(real_match_rule,s2))
print(re.match(real_match_rule,s3))
print(re.match(real_match_rule,s4))
print(re.match(real_match_rule,s5))
print(re.match(real_match_rule,s6))
print(re.match(real_match_rule,s7))
print(re.match(real_match_rule,s8))

