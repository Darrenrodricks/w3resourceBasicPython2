# Write a Python program to create a sequence where the first four members of
# the sequence are equal to one, and each successive term of the sequence is equal to the
# sum of the four previous ones. Find the Nth member of the sequence.
def first_four(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    return first_four(n-1) + first_four(n-2) + first_four(n-3) + first_four(n-4)

print(first_four(5))
print(first_four(6))
print(first_four(7))
