def largest(min_factor, max_factor):
    return find_best(min_factor, max_factor, lambda x,y: x > y)


def smallest(min_factor, max_factor):
    return find_best(min_factor, max_factor, lambda x,y: x < y)


def find_best(min_factor, max_factor, comp):
    # uses the 'comp' function to determine whether to throw out previous best
    # if comp(new_prod, prev_best) is True, then new_prod becomes the new best
    if min_factor > max_factor:
        raise ValueError("min_factor larger than max_factor")
    best = None
    factors = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            test = i*j
            if is_palindrome(i*j):
                if best is None or comp(test, best): 
                    best = test
                    factors = [[i,j]]
                elif test == best:
                    factors.append([i,j])


    return (best, factors)


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]
