def saddle_points(matrix):
    num_rows = len(matrix)
    if num_rows == 0:
        return []
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError('Invalid matrix: Rows are not all same length')
    
    row_maxes = [max(row) for row in matrix]
    col_mins = [min([row[i] for row in matrix]) for i in range(num_cols)]
    
    saddles = []
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == row_maxes[i] and matrix[i][j] == col_mins[j]:
                saddles.append({'row': i+1, 'column': j+1})
    
    return saddles
