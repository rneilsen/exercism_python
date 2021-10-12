try:
    from sympy import proper_divisors
except ImportError:
    def proper_divisors(number):
        divisors = []
        for n in range(1, number):
            if number % n == 0:
                divisors.append(n)
        return divisors

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
    