#!/usr/bin/python3
y = 0
for j in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(j - y)), end="")
    y = 32 if y == 0 else 0
