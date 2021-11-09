def is_valid(isbn):
    scrubbed = isbn.replace('-', '')

    if len(scrubbed) != 10:
        return False
    if not scrubbed[:-1].isnumeric():
        return False

    digits = [int(c) for c in scrubbed[:-1]]

    if scrubbed[-1].isdigit():
        digits.append(int(scrubbed[-1]))
    elif scrubbed[-1] == 'X':
        digits.append(10)
    else:
        return False

    return (sum([x*i for (x,i) in zip(digits, range(10,0,-1))]) % 11 == 0)
