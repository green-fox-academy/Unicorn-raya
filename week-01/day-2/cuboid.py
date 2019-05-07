# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

length = 100
width = 10
height = 9

Surface_Area = (length * width + length * height + width * height) * 2
Volume = length * width * height

print(f'Surface Area: {Surface_Area}\nVolume: {Volume}')