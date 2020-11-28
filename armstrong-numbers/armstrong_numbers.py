def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    return number == sum([digit**num_digits for digit in digits])
