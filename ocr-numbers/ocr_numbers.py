# Create a dict (DIGITS): key = each digit as pipes and underscores, val = integer

RAW_DIGITS = '''
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
                              '''
DIGITS = {'\n'.join( [row[3*n:3*n+3] for row in RAW_DIGITS.splitlines()[1:]] ) : str(n)
        for n in range(10)}

def convert(input_grid):
    return DIGITS['\n'.join(input_grid)]