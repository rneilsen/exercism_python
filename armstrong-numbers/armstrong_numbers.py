def is_armstrong_number(number):
    digits = [int(c) for c in str(number)]
    num_digits = len(digits)
    return (number == sum([d**num_digits for d in digits]))
