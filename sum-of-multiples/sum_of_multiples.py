def sum_of_multiples(limit, multiples):
    used_mults = set()
    sum = 0

    for n in multiples:
        if n == 0:
            continue
        i = n
        while i < limit:
            if i not in used_mults:
                sum += i
                used_mults.add(i)
            i += n
    
    return sum
