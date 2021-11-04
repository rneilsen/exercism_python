from itertools import combinations_with_replacement

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    max_coins = 1 + target // min(coins)
    i = 0
    while i < max_coins:
        combos = combinations_with_replacement(coins, i)
        for combo in combos:
            if sum(combo) == target:
                return sorted(combo)
        i += 1

    raise ValueError("can't make target with given coins")
