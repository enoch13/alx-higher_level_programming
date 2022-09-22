#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for n in sys.argv:
        if n != sys.argv[0]:
            sum += int(n)
            print("{:d}".format(sum))
