from itertools import product

WHITE = 'W'
BLACK = 'B'
NONE = ' '

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        rows = [[('' if ch==' ' else ch) for ch in row] for row in board]
        self.width = len(board[0])
        self.height = len(board)

    def get_neighbours(self, x, y):
        neighbours = set()
        valid_x = set(range(self.width)).intersection({x-1, x+1})
        neighbours.update(set([(xc, y) for xc in valid_x]))
        valid_y = set(range(self.height)).intersection({y-1, y+1})
        neighbours.update(set([(x, yc) for yc in valid_y]))
        return neighbours

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass

