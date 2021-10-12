"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 3
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    if list_one == list_two: return EQUAL
    
    swapped = False
    if len(list_one) > len(list_two):
        swapped = True
        (list_one, list_two) = (list_two, list_one)
    
    (len_one, len_two) = (len(list_one), len(list_two))

    for i in range(len_two - len_one + 1):
        if list_two[i:i+len_one] == list_one:
            return (SUPERLIST if swapped else SUBLIST)
    
    return UNEQUAL
