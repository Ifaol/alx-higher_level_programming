#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
def calculate_result(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
if __name__ == "__main__":
    n = len(sys.argv)
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        result = calculate_result(a, operator, b)
        print("{} {} {} = {}".format(a, operator, b, result))
