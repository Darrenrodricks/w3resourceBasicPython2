# Given a list of numbers, return True if first and last number of a list is same
def first_checker(numberList):
    print("Given list is ", numberList)
    a = numberList[0]
    b = numberList[-1]
    if (a == b):
        return True
    else:
        return False

numList = [10, 20, 30, 40, 10]
print("result is {}".format(first_checker(numList)))