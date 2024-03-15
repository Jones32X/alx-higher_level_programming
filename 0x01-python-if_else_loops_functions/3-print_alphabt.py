#!/usr/bin/python3
for lowercaseLetter in range(97, 123):
    if lowercaseLetter == 101:
        continue
    elif lowercaseLetter == 113:
        continue
    print("{}".format(chr(lowercaseLetter)), end="")
