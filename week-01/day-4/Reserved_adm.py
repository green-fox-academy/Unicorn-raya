# Reserved admin
# Create a regular expression that matches if for the following words:

# Admin
# admin

import re
a = re.compile(r'[Aa]dmin')
print(re.match(a,"Admin"))
print(re.match(a,"admin"))
print(re.match(a,"aDmm"))
