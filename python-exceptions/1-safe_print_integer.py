#!/usr/bin/python3
def safe_print_integer(value):
    printed = 0
    if(my_list):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                printed += 1
            except(ValueError, TypeError):
                pass
    print()
    return(printed)
