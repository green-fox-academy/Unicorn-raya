"""
Anagram
What the hell is an anagram?
An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; for example, the word anagram can be rearranged into nag-a-ram. [for more detail check anagram on Wikipedia]

Exercise
Create a function named is anagram following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.

Examples
input 1	input 2	output
"dog"	"god"	true
"green"

"""

def Anagram(phrase_1, phrase_2):
    return sorted(phrase_1) == sorted(phrase_2)

print(Anagram("Timberman","iTmberman"))
print(Anagram("decade","ex-aid"))