#!/usr/bin/python3
s = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
s = " ".join([s.split()[5], s.split()[6], s.split()[12], s.split()[0]])
print(s)
