#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0

    for value in my_list[:x]:
        try:
            print("{}".format(value), end='')
            number += 1
        except ValueError:
            pass

    print()
    return number
