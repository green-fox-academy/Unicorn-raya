# Image source
# Create a regular expression that matches the source from HTML image element.

# Task	Text	Capture Groups
# Capture	<img src="dog.png">	dog.png
# Capture	<img alt="Cat picture" src="./images/cat-01.png">	./images/cat-01.png
# Skip	<script src="jquery.js"></script>

import re
r = re.compile(r'<img.*src="(.*\.png)')
Test_string = ['<img src="dog.png">', '<img alt="Cat picture" src="./images/cat-01.png">', '<script src="jquery.js"></script>']
for matches_values in Test_string:
    result = re.match(r,matches_values)
    if result:
        print(f'{matches_values}: {result.groups()}')
    else:
        print("not match")
