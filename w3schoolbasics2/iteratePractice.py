# Given a range of the first 10 numbers, Iterate from the start number to the end
# number, and In each iteration print the sum of the current number and previous number
for i in range(1, 10):
    print("Current Number: {}, Previous Number: {}, Sum: {}".format(i, i-1, i + (i - 1)))