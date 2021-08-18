def annotate(minefield):
    # Function body starts here
    lengths = [len(row) for row in minefield]
    if max(lengths) != min(lengths):
        raise ValueError("Invalid board - rows not equal length")
    
