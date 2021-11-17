def flatten(iterable):
    result = []
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result
