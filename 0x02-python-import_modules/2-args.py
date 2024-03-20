#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    ARGLen = len(sys.argv)

    if (ARGLen == 0):
        print("0 arguments.")
    elif (ARGLen == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(ARGLen))
        number = 1
        for argument in sys.argv:
            print("{:d}: {}".format(number, argument))
            number = number + 1
