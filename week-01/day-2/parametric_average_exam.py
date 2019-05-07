# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4


number = int(input("Input epoch times: "))
sum,avg = 0,0
for i in range(number):
    sum += int(input("Enter number: "))
avg = sum / number

print(f'Sum: {sum}, Average: {avg}')
