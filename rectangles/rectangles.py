def rectangles(strings):
    if len(strings) == 0: return 0

    height, width = len(strings), len(strings[0])
    num = 0

    for row_num in range(height):
        for col_num in range(width):
            if strings[row_num][col_num] == '+':
                num += rectangles_from_top_left(
                        [row[col_num:] for row in strings[row_num:]]
                )
    return num


def rectangles_from_top_left(rows):
    num = 0
    top_row = rows[0]

    for j in range(1, len(top_row)):
        if top_row[j] == '+':
            # search the block below this section of the top row
            num += rectangles_below([row[:j+1] for row in rows])
        elif top_row[j] == '-':
            continue
        else:
            return num
    return num


def rectangles_below(rows):
    num = 0
    for i in range(1, len(rows)):
        if (rows[i][0], rows[i][-1]) == ('+', '+'):
            # got all 4 corners, if bottom row is complete we've got one
            if set(rows[i]).issubset({'+', '-'}):
                num += 1
        elif (rows[i][0], rows[i][-1]) in {('|', '|'), ('+', '|'), ('|', '+')}:
            continue
        else:
            # one or the other side is broken, abandon this block
            return num
    return num
