#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    i = len(sys.argv) - 1
    if (i == 0):
        print("{:d} arguments.".format(i))
    elif (i == 1):
        print("{:d} argument:".format(i))
    else:
        print("{:d} arguments:".format(i))
    for i in range(1, size):
        print("{:d}: {}".format(i, sys.argv[i]))
