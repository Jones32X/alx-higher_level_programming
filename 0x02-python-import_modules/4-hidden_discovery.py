#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    dat = dir(hidden_4)
    for name in dat:
        if name[:2] != "__":
            print(name)
