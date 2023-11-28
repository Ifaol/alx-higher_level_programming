#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
str = "Last digit of {} is {} and is {}"
if number < 0:
    num = -num
if num == 0:
    print(str.format(number, num, "0"))
elif num < 6:
    print(str.format(number, num, "less than 6 and not 0"))
else:
    print(str.format(number, num, "greater than 5"))
