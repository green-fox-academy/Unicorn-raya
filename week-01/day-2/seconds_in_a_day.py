current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables 

day_seconds = 24 * 60 * 60
remain_seconds = day_seconds - (current_hours * 60 + current_minutes) * 60

print(remain_seconds)