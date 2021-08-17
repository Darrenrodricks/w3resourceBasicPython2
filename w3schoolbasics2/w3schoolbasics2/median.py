numbers = []
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter another number: "))
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.sort()
print("The median of the numbers given was {}".format(numbers[1]))
