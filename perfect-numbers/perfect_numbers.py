from sympy import proper_divisors

def classify(number):
    if number < 1:
        raise ValueError("Input must be positive integer")
    
    divsum = sum(proper_divisors(number))
    if divsum < number:
        return "deficient"
    elif divsum > number:
        return "abundant"
    else:
        return "perfect"
    