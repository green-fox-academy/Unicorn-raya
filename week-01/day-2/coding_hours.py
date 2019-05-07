# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

Daily_work_hours = 6
Semester = 17
Weekdays = 5
Week = 7
Weekly_work_hour = 52

print(f'Coding hours in this semester is {Daily_work_hours * Weekdays * Semester }')
print(f'Percentage of the coding hours in the semester is {int(Daily_work_hours * Weekdays/Weekly_work_hour * 100)}%')