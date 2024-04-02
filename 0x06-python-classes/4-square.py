#!/usr/bin/python3

Square = __import__('4-square').Square

the_square = Square(89)
print("Area: {} for size: {}".format(the_square.area(), the_square.size))

the_square.size = 3
print("Area: {} for size: {}".format(the_square.area(), the_square.size))

try:
    the_square.size = "5 feet"
    print("Area: {} for size: {}".format(the_square.area(), the_square.size))
except Exception as e:
    print(ei)
