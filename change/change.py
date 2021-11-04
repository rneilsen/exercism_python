def find_fewest_coins(coins, target):
    coins = sorted(coins)
    change = []

    if target < 0:
        raise ValueError("target can't be negative")
    while target > 0 and len(coins) > 0:
        coin = coins.pop()
        while coin <= target:
            target -= coin
            change.append(coin)
    if target != 0:
        raise ValueError("can't make target with given coins")
    return change
