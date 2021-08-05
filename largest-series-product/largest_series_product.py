from math import prod

def largest_product(series, size):
    if size < 0 or size > len(series):
        raise ValueError("Invalid size given")
    digits = [int(ch) for ch in series]
    return max( [ prod( digits[i:i+size] ) 
            for i in range(len(digits) - size + 1) ] )
