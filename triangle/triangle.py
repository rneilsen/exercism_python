def equilateral(sides):
    if not test_valid(sides): return False
    return len(set(sides)) == 1


def isosceles(sides):
    if not test_valid(sides): return False
    return len(set(sides)) <= 2


def scalene(sides):
    if not test_valid(sides): return False
    return len(set(sides)) == 3


def degenerate(sides):
    if not test_valid(sides): return False
    s_sides = sides.sort()
    return s_sides[0] + s_sides[1] == s_sides[2]


def test_valid(sides):
    if min(sides) <= 0:
        return False        
    s_sides = sorted(sides)
    if s_sides[0] + s_sides[1] < s_sides[2]:
        return False
    return True
