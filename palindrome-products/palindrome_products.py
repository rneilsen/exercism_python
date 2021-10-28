def largest(min_factor, max_factor):
    best = find_best(min_factor, max_factor, smallest=False)
    return (best, find_factors(best, min_factor, max_factor))
    

def smallest(min_factor, max_factor):
    best = find_best(min_factor, max_factor, smallest=True)
    return (best, find_factors(best, min_factor, max_factor))


def find_best(min_factor, max_factor, smallest):
    if min_factor > max_factor:
        raise ValueError("min_factor larger than max_factor")
    
    if smallest:
        (start, stop, step) = (min_factor, max_factor + 1, 1)
    else:
        (start, stop, step) = (max_factor, min_factor - 1, -1)

    i = start
    best = None
    while i != stop:
        j = start
        jstop = i + step
        while j != jstop:
            if is_palindrome(i*j):
                if best is None:
                    best = i*j
                elif smallest:
                    best = min(best, i*j)
                else:
                    best = max(best, i*j)
            j += step
        i += step
        if best is not None:
            # abort search if i*(starting j value) can't ever surpass best
            if (smallest and i * start > best) or (not smallest and i * start < best):
                break
    return best


def find_factors(num, min, max):
    if num is None:
        return []
    
    return [(i, num // i)
            for i in range(min, max + 1)
            if num % i == 0 and num // i in range(min, max + 1)]


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]
