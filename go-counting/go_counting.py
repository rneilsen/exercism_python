from itertools import product

WHITE = 'W'
BLACK = 'B'
NONE = ''

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.rows = [[(NONE if ch==' ' else ch) for ch in row] for row in board]
        self.width = len(board[0])
        self.height = len(board)

    def get_space(self, x, y):
        return self.rows[y][x]

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
        if x not in range(self.width) or y not in range(self.height):
            raise ValueError("Invalid coordinates")

        if self.get_space(x,y) != '': 
            # designated space is a stone, not territory
            return (NONE, set())
        
        checked = {(x,y)}
        territory = checked.copy()
        unchecked = self.get_neighbours(x,y)
        owners = set()
        while len(unchecked) > 0:
            space = unchecked.pop()
            space_cont = self.get_space(*space)
            if space_cont == NONE:
                unchecked.update(self.get_neighbours(*space).difference(checked))
                territory.add(space)
            else:
                owners.add(space_cont)
            checked.add(space)
        if len(owners) == 1:
            return (owners.pop(), territory)
        else:
            return (NONE, territory)


    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        terrs = {NONE: set(), WHITE: set(), BLACK: set()}
        unchecked = set(product(range(self.width), range(self.height)))
        while len(unchecked) > 0:
            space = unchecked.pop()
            (owner, terr) = self.territory(*space)
            terrs[owner].update(terr)
            unchecked.difference_update(terr)
        return terrs

