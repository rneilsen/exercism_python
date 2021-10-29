from itertools import product

def annotate(minefield):
    lengths = {len(row) for row in minefield}
    if len(lengths) > 1:
        raise ValueError("Invalid board - rows not equal length")
    if not set(''.join(minefield)).issubset({' ', '*'}):
        raise ValueError("Invalid characters in board")

    annot_board = []
    for i in range(len(minefield)):
        new_row = []
        for j in range(len(minefield[0])):
            if minefield[i][j] == '*':
                new_row.append('*')
            else:
                adj_mines = count_adj_mines(minefield, i, j)
                new_row.append(' ' if adj_mines == 0 else str(adj_mines))
        annot_board.append(''.join(new_row))
    return annot_board


def count_adj_mines(minefield, row, col):
    (height, width) = (len(minefield), len(minefield[0]))
    adj_mines = 0
    neighbour_spaces = product(
            range(max(row-1, 0), min(row+2, height)) ,
            range(max(col-1, 0), min(col+2, width)) )
    for h, k in neighbour_spaces:
        adj_mines += (1 if minefield[h][k] == '*' else 0)
    return adj_mines
