def square_of_sum(number):
    # square of (n^2+n)/2 formula
    return ((number**2 + number) / 2)**2


def sum_of_squares(number):
    # closed form of square pyramidal number
    return number * (number+1) * (2*number+1) / 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
