def is_isogram(string):
    scrubbed = list(filter(lambda c: c.isalpha(), string.lower()))
    return len(scrubbed) == len(set(scrubbed))

is_isogram("thumbscrew-japingly")