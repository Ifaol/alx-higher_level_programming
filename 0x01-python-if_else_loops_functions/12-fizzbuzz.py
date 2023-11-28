#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        val1 = n % 3
        val2 = n % 5
        if val1 == 0 and val2 == 0:
            print("{}".format("FizzBuzz"), end = " ")
        elif val1 == 0:
            print("{}".format("Fizz"), end=" ")
        elif val2 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(n), end=" ")
