def num_distinct(stuff):
    return len(set(stuff))


def equilateral(sides):
    if not test_valid(sides): 
        return False
    return num_distinct(sides) == 1


def isosceles(sides):
    if not test_valid(sides): 
        return False
    return num_distinct(sides) <= 2


def scalene(sides):
    if not test_valid(sides): 
        return False
    return num_distinct(sides) == 3


def degenerate(sides):
    if not test_valid(sides): 
        return False
    s_sides = sorted(sides)
    return s_sides[0] + s_sides[1] == s_sides[2]


def test_valid(sides):
    if min(sides) <= 0:
        return False        
    s_sides = sorted(sides)
    if s_sides[0] + s_sides[1] < s_sides[2]:
        return False
    return True
