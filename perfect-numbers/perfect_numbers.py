from sympy import divisors

def classify(number):
    if number < 1:
        raise ValueError("Input must be positive integer")
    
    divsum = sum(divisors(number)[:-1])
    if divsum < number:
        return "deficient"
    elif divsum > number:
        return "abundant"
    else:
        return "perfect"
    