# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
def remove_third(data):
    len_list = (len(data))
    while len_list > 0:
        del(data[2])
        print(data)
        len_list -= 1

remove_third([10,20,30,40,50,60,70,80,90])

