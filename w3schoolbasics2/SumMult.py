# Given two integer numbers return their product. If the product is greater than 1000, then return their sum
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))

if a * b >= 100:
    print(a + b)
else:
    print(a * b)