def slices(series, length):
    if length > len(series):
        raise ValueError("slice length cannot be longer than series length")
    if length < 1:
        raise ValueError("slice length cannot be less than 1")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    
    return [series[i:i+length] for i in range(len(series) - length + 1)]
