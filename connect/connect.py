from itertools import product

class ConnectGame:
    def __init__(self, board):
        self.board = [row.strip().split(' ') for row in board.splitlines()]
        self.height = len(self.board)
        self.width = len(self.board[0])


    def get_neighbours(self, row, col):
        standard_steps = {(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)}
        standard_neighbours = {(row + rstep, col + cstep) for (rstep, cstep) in standard_steps}

        valid_neighbours = set(product(
                range(max(0, row - 1), 1 + min(self.height - 1, row + 1)),
                range(max(0, col - 1), 1 + min(self.width - 1, col + 1)) 
        ))

        return standard_neighbours.intersection(valid_neighbours)


    def are_groups_connected_by(self, symbol, set1, set2):
        """Tests whether there is a contiguous block of cells containing a 
        given symbol that contains cells in both groups"""
        set1 = {(r, c) for (r, c) in set1 if self.board[r][c] == symbol}
        set2 = {(r, c) for (r, c) in set2 if self.board[r][c] == symbol}

        while len(set1) > 0:
            checked_cells = set()
            connected_alike_block = set()

            check_cell = set1.pop()
            check_queue = {check_cell}

            while len(check_queue) > 0:
                check_row, check_col = check_queue.pop()
                checked_cells.add((check_row, check_col))

                if self.board[check_row][check_col] == symbol:
                    if (check_row, check_col) in set2:
                        return True

                    connected_alike_block.add((check_row, check_col))
                    check_neighbours = self.get_neighbours(check_row, check_col)
                    check_queue.update(check_neighbours - checked_cells)

            set1 -= checked_cells

        return False


    def get_winner(self):
        # Check for O win (top to bottom)
        top_row = {(0,i) for i in range(self.width)}
        bottom_row = {(self.height - 1, i) for i in range(self.width)}
        if self.are_groups_connected_by('O', top_row, bottom_row):
            return 'O'

        # Check for X win (left to right)
        left_col = {(i, 0) for i in range(self.height)}
        right_col = {(i, self.width - 1) for i in range(self.height)}
        if self.are_groups_connected_by('X', left_col, right_col):
            return 'X'

        # No win yet
        return ''
