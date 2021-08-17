floatNumbers = []
n = int(input("Enter the list size : "))

for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("User List is {}".format(floatNumbers))