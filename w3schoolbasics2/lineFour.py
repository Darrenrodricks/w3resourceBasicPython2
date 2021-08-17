# if the number is divisble by 3 print fizz, by 5 printt buzz and by 15 print fizz buzz

for i in range(31):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 15 == 0:
        print("fizzbuzz")
        