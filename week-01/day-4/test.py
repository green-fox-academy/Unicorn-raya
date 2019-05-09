import re
my_string = "hello"
p = re.compile('hello')

#concrete string and compile
p.match('hello world')
p.match('0 hello')

#character set [] (^)
print(re.match('[abc]','a'))
re.match('[a-z]','tad')

re.match['[\w]','tad']
re.match['\\\\section','\section'] #\s is ?
"a?b"# ? means 0?1
 "a.b" # means anything a-z
 'a{1,2}b' True if a a b false if aaaaaaaab {min_number, max_number}
#repetition + * ? {m,n}
[abc]+ abc/tv abc

#matching(match ,search, findall finditer)
print(p.search(my_string))
print(re.findall("[abc+]","abcade anssnasna"))

#match object (None, group, start,end ,span)
my_string = "this is levi: 114514 is a mentor"
re.match('[\d]+',my_string) #it is search~ (difference?)
print(m) # None
print(
    m.end(),
    m.span(),
    m.group(),
)

#module- level function (match , search , findall)
a = re.compile('[abc]')
p.match('a')

re.match('[abc]','a')

for i in range(1000): p.match('a') #1 time
for i in range(1000): p.match("abc",'a')# 1000 times

#replacing match(sub)
my_string = "ray's id is 1312321312312"
re.sub('[\d]+','<sensitive data>',my_string)

#groups(non-capturing)
my_string = 'the weather is is nice'
re.search('ab',my_string) #once time

re.search(r'(\w+)\s\1',my_string) #once time

re.search()