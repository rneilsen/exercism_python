def encode(numbers):
    output = []
    for n in numbers:
        if n == 0:
            output.append(0)
            continue

        pieces = []
        while n > 0:
            pieces.append(n % 128)
            n //= 128

        # set first bit 0 for all-but-first piece (first piece will become last)
        for i in range(1, len(pieces)):
            pieces[i] += 128

        output += pieces[::-1]

    return output


def decode(bytes_):
    if bytes_[-1] >= 128:
        raise ValueError("incomplete sequence")

    output = []
    num_constructor = []
    for byte in bytes_:
        num_constructor.append(byte % 128)

        if byte < 128:
            # this byte has first bit 0, so calc and append total, then reset
            num_constructor.reverse()
            output.append(sum([b*(128**i) for (i,b) in enumerate(num_constructor)]))
            num_constructor = []

    return output
