# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.

number = int(input("Please input a digital number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")