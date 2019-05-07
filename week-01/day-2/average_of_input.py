# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

count,sum_number,loop_times = 0,0,5 
while count < loop_times:
    sum_number += int(input())
    count += 1
avg = sum_number / loop_times

print(f'Sum: {sum_number}, Average: {avg}')