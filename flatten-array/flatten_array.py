def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list):
            result += flatten(item)
        elif item is not None:
            result.append(item)
    return result
