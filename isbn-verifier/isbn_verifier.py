def is_valid(isbn):
    """Determines whether a given ISBN-format number is valid"""
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

    isbn_checksum = sum([x*i for (x,i) in enumerate(digits[::-1], start=1)])
    return isbn_checksum % 11 == 0
