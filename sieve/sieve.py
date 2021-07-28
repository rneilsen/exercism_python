def primes(limit):
    if limit < 2:
        return []
    elif limit == 2:
        return [2]
    numbers = [False, False] + [True] * (limit - 1)

    prime_list = [2]
    cur_prime = 3
    while cur_prime <= limit:
        # find next cur_prime
        while cur_prime <= limit and not numbers[cur_prime]:
            cur_prime += 2
        if cur_prime > limit:
            break
        prime_list.append(cur_prime)

        # knock out all multiples of cur_prime
        n = cur_prime * 2
        while n <= limit:
            numbers[n] = False
            n += cur_prime

        cur_prime += 2
    return prime_list
