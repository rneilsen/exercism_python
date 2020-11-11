def steps(number):
    if number < 1:
        raise ValueError("Positive integers only")
    return collatz(number)


def collatz(number):
    if number == 1:
        return 0
    elif number % 2 == 0:   # even
        return 1 + collatz(number / 2)
    else:   # odd
        return 1 + collatz(3*number + 1)
