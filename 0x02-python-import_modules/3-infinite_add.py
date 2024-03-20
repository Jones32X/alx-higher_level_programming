#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sys.argv.pop(0)
    tot = 0
    for num in sys.argv:
        tot += int(num)
        print("{}".format(tot))
