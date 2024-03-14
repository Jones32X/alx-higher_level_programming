#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if lastdigit > 0:
    print("{} is positive".format(lastdigit))
if lastdigit == 0:
    print("{} is zero".format(lastdigit))
if lastdigit < 0:
    print("{} is negative".format(lastdigit))
