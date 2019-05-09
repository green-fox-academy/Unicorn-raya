# Create a regular expression that matches all Green Fox Academy email address.

# Task	Text	Capture Groups
# Capture	john@greenfoxacademy.com	john
# Capture	jane.doe@greenfoxacademy.com	jane.doe
# Capture	jane@greenfox.academy	jane
# Skip	john@wick.com	
# Skip	jane@citromail.hu	
# Skip	janegreenfoxacademy.com	


#rule name + @ + greenfox * .  
import re
real_match_rule = re.compile(r'.*@greenfox.*')

s1="john@greenfoxacademy.com"
s2="jane.doe@greenfoxacademy.com"
s3="jane@greenfox.academy"
s4="john@wick.com"	
s5="jane@citromail.hu"	
s6="janegreenfoxacademy.com"

print(re.match(real_match_rule,s1))
print(re.match(real_match_rule,s2))
print(re.match(real_match_rule,s3))
print(re.match(real_match_rule,s4))
print(re.match(real_match_rule,s5))
print(re.match(real_match_rule,s6))