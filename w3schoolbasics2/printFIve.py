# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def findDivisible(n):
    print("list: {}".format(n))
    for num in n:
        if (num % 5 == 0):
            print(num)

numList = [10, 20, 33, 46, 55]
findDivisible(numList)