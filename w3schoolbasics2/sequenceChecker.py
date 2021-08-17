# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def sequence_checker(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print(sequence_checker([1,5,7,9]))
print(sequence_checker([2,4,5,5,7,9]))