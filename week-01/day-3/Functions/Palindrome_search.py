"""
Palindrome searcher
What the hell is a palindrome?

Exercise
Create a function named search palindrome following your current language's style guide. It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes.

Examples
input	output
"dog goat dad duck doodle never"	["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
"apple"	[]
"racecar"	["racecar", "aceca", "cec"]
""	[]
"""

def is_palindrom(phase):
    phase_length = len(phase)
    if phase_length == 0:
        return False
    else:
        for index in range(phase_length):
            if phase[index] == phase[phase_length - 1 - index]:
                continue
            else:
                return False
    return True


def Palindrome_search(phase):
    lst = []
    phase_length = len(phase)
    if phase_length == 0 or phase_length == 1:
        return lst
    else:
        #odd length of Palindrome
        #start from the second index, loop times is length - 1
        offset = 1
        for pointer in range(1,phase_length):
            while pointer - offset > -1 and pointer + offset < phase_length and phase[pointer + offset] == phase[pointer - offset]:
            #ensure the move of the pointer within phase                                ensure left == right      
                lst.append(phase[ pointer - offset : pointer + offset + 1])
                offset += 1      
            offset = 1
            pointer += 1    
        #even length of Palindrome
        if phase_length < 4:
            return lst
        # two pointer start from second and third place, loop times should be length - 1 - 1  
        offset = 1
        for pointer_1 in range(1,phase_length - 1):
            pointer_2 = pointer_1 + 1
            while pointer_1 - offset > -1 and pointer_2 + offset < phase_length and phase[pointer_1] == phase[pointer_2] and phase[pointer_1 - offset] == phase[pointer_2 + offset]:
                print(str(pointer_1 - offset) +" " + str(pointer_2 + offset))
                lst.append(phase[pointer_1 - offset: pointer_2 + offset + 1])
                offset += 1
            offset = 1
            pointer_1 += 1

    return lst
print(Palindrome_search("dog goat dad duck doodle never"))
#should be ["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
print(Palindrome_search("racecar"))
print(Palindrome_search(""))
print(Palindrome_search("apple"))