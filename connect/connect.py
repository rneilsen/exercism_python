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


    def get_winner(self):
        pass
