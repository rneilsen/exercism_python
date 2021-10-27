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
                range(max(0, col - 1), 1 + min(self.width - 1, col + 1)) ))

        return standard_neighbours.intersection(valid_neighbours)


    def get_connected_alike_block(self, row, col):
        search_type = self.board[row][col]
        check_queue = list(self.get_neighbours(row, col))
        checked_cells = {(row, col)}
        connected_alike_block = {(row, col)}

        while len(check_queue) > 0:
            (check_row, check_col) = check_queue.pop()
            checked_cells.add((check_row, check_col))
            
            if self.board[check_row][check_col] == search_type:
                connected_alike_block.add((check_row, check_col))
                check_neighbours = self.get_neighbours(check_row, check_col)
                check_queue.extend(check_neighbours.difference(checked_cells))
        
        return connected_alike_block


    def get_winner(self):
        pass
