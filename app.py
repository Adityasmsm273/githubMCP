import os
import sys

def calculate_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

def main():
    radius = input("Enter the radius of the circle: ")
    area = calculate_area(radius)
    print("The area is: " + area)

main()
