#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sys.argv.pop(0)
    tot = 0
    for num in sys.argv:
        tot = tot + int(num)
    print("{}".format(tot))
