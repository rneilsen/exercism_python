from typing import List

def triplets_with_sum(number: int) -> List[List[int]]:
    """Returns a list of all Pythagorean triples having the given sum"""
    triplets = []
    primitive_queue = [[3,4,5]]
    while len(primitive_queue) > 0:
        (a,b,c) = primitive_queue.pop()
        if number % sum((a,b,c)) == 0:
            k = number // sum((a,b,c))
            triplets.append(sorted([k*a, k*b, k*c]))

        children = calc_child_primitives(a,b,c)
        for child in children:
            if sum(child) <= number:
                primitive_queue.append(child)
    return triplets

def calc_child_primitives(a,b,c) -> List[List[int]]:
    """Uses the Berggren transformations to produce primitive pythagorean
    triples from a given triple, the resulting tree includes every primitive
    triple exactly once"""
    return [[a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c],
            [a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c],
            [-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c]]
