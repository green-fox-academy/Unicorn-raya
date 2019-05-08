# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

insert_place_1 = quote.find("It")
insert_place_2 = quote.find("you")
quote = quote[:insert_place_1 + 3] + "always takes longer than " + quote[insert_place_2:]

print(quote)

