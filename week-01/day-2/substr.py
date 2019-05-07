#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one

def substr(target, keyword):
    keyword_length = len(keyword)
    str_length = len(target)
    keyword_index = 0
    #dic = {}
    if keyword_length > str_length:
        return -1
    for i in range(str_length):
        if target[i] == keyword[keyword_index]:
            #print(f"current i is : {i}")
            keyword_index += 1
        else:
            keyword_index = 0
        if keyword_index == keyword_length:
            return i - keyword_length + 1
    return -1
        

# check kmp

#  Example
# should print: `17`
print(substr("this is what I'm searching in", "wh"))

print("-------------------------------------------------")

# should print: `-1`
print(substr("this is what I'm searching in", "not"))