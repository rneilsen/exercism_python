def square(number):
    if number < 1 or number > 64:
        raise ValueError('Squares are numbered 1-64')
    return 2**(number-1)


def total():
    return 2**64 - 1    # sum of 2^i for i in [0,1,2,...,n-1] equals 2^n - 1
