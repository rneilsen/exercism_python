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

    words = []
    p = 0
    while number > 0:
        if number % 1000 != 0:
            words = block_name(number % 1000) + [powers[p]] + words
        p += 3
        number //= 1000

    return ' '.join([word for word in words if word != ''])


def block_name(number):
    """Constructs name of integer from 1 to 999 inclusive as a list of words"""
    name = []
    if number >= 100:
        name += [names[number // 100], 'hundred']
        number %= 100

    if number in names:
        return name + [names[number]]

    return name + [names[10 * (number // 10)] + '-' + names[number % 10]]
