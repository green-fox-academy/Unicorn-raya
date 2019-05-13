# Post-it
# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class PostIt(object):
    background_color = "None"
    text = ""
    text_color = ""

eg_1 = PostIt()
eg_2 = PostIt()
eg_3 = PostIt()

eg_1.background_color = "orange"
eg_1.text = "idea1"
eg_1.text_color = "blue"

eg_2.background_color = "pink"
eg_2.text = "Awesome"
eg_2.text_color = "black"

eg_3.background_color = "Yellow"
eg_3.text = "black"
eg_3.text_color = "Superb"

print(f"eg1: {eg_1.background_color},{eg_1.text},{eg_1.text_color}")
print(f"eg2: {eg_2.background_color},{eg_2.text},{eg_2.text_color}")
print(f"eg3: {eg_3.background_color},{eg_3.text},{eg_3.text_color}")

