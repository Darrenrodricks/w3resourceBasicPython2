# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(' '.join(char_list))

# from itertools import permutations
#
# # Get all combination of [1, 2, 3]
# # of length 3
# comb = permutations(['a','e','i','o','u'], 5)
#
# for i in comb:
#     print(i)