# Write a Python program to get the third side of right angled triangle from two given sides.
import math
side_a = float(input("Please enter the length of the first side: "))
side_b = float(input("Please enter the length of the second side: "))
c = math.sqrt(((side_a ** 2) + (side_b ** 2)))
print("Your third side length is: {}".format(c))