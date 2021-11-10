names = { 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

powers = {0: '', 3: 'thousand', 6: 'million', 9: 'billion'}


def say(number):
    """Returns the English name of a given integer"""
    if not (0 <= number < 10**12):
        raise ValueError("Number out of range")
    if number == 0:
        return 'zero'

    words = rec_say(number)
    while '' in words:
        words.remove('')

    return ' '.join(words)


def rec_say(number):
    """Constructs the name of a positive integer as a list of words"""
    if number == 0:
        return []

    n = 0
    while number >= 1000**(n+1):
        n += 1

    this_block = number // (1000**n)
    remainder = number % 1000**n

    return block_name(this_block) + [powers[3*n]] + rec_say(remainder)


def block_name(number):
    """Constructs name of integer from 1 to 999 inclusive as a list of words"""
    name = []
    if number >= 100:
        name += [names[number // 100], 'hundred']
        number %= 100

    if number in names:
        return name + [names[number]]

    return name + [names[10 * (number // 10)] + '-' + names[number % 10]]
