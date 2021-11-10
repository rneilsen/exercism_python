names = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

powers = {0: '', 3: ' thousand', 6: ' million', 9: ' billion'}


def say(number):
    if not (0 <= number < 10**12):
        raise ValueError("Number out of range")
    if number == 0:
        return 'zero'

    return rec_say(number)


def rec_say(number):
    if number == 0:
        return ''

    n = 0
    while number >= 1000**(n+1):
        n += 1

    if number < 1000:
        return block_name(number)

    this_block_name = block_name(number // (1000**n)) + powers[3*n]
    remainder_name = rec_say(number % 1000**n)

    return this_block_name + (' ' + remainder_name if remainder_name else '')


def block_name(number):
    """names numbers from 1 to 999 inclusive"""
    if not 1 <= number <= 999:
        raise ValueError

    name = ''

    if number >= 100:
        name += names[number // 100] + ' hundred'
        number %= 100

    if number == 0: return name

    if name: name += ' '

    if number in names:
        return name + names[number]

    return name + names[number - number % 10] + '-' + names[number % 10]
