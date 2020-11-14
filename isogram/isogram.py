def is_isogram(string):
    scrubbed = [c for c in string.lower() if c.isalpha()]
    return len(scrubbed) == len(set(scrubbed))
