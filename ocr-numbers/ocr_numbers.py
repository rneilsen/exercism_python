# Create a dict (DIGITS): key = each digit as pipes and underscores, val = integer

RAW_DIGITS = '''
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
                              '''
DIGITS = {'\n'.join( [row[3*n:3*n+3] for row in RAW_DIGITS.splitlines()[1:]] ) : str(n)
        for n in range(10)}

def convert(input_grid):
    if len(input_grid) < 4 or len(input_grid) % 4 != 0:
        raise ValueError("Invalid input grid size")
    lengths = [len(line) for line in input_grid]
    if len(set(lengths)) != 1 or lengths[0] % 3 != 0:
        raise ValueError("Invalid input grid size")



    return DIGITS.get('\n'.join(input_grid), '?')