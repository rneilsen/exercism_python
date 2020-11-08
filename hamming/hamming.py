def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("String lengths must be the same")
    dist = 0
    for (a_char, b_char) in zip(strand_a, strand_b):
        if a_char != b_char:
            dist += 1
    return dist
