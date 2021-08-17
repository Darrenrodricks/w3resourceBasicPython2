# Write a Python program to find the number of divisors of a given integer is even or odd.
def divisor_checker(n):
        x = len([i for i in range(1,n+1) if not n % i])
        return x
print(divisor_checker(15))
print(divisor_checker(12))
print(divisor_checker(9))
print(divisor_checker(6))
print(divisor_checker(3))
