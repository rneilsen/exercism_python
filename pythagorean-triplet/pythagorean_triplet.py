def triplets_with_sum(number):
    triplets = []
    for a in range(3, number // 3):
        for b in range(a+1, 2 * (number // 3)):
            c = number - (a+b)
            if a**2 + b**2 == c**2:
                triplets.append([a,b,c])
            elif a**2 + b**2 > c**2:
                break
    return triplets
