from itertools import product
from typing import Set, Tuple, Dict
Coords = Tuple[int, int]

WHITE = 'W'
BLACK = 'B'
NONE = ''

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: str) -> None:
        self.rows = [[(NONE if ch==' ' else ch) for ch in row] for row in board]
        self.width = len(board[0])
        self.height = len(board)
        self.valid_spaces = set(product(range(self.width), range(self.height)))

    def get_space_content(self, x: int, y: int) -> str:
        """Returns the content of a specific space on the board ('B', 'W', or '')"""
        return self.rows[y][x]

    def get_neighbours(self, x: int, y: int) -> Set[Coords]:
        """Returns a set of the valid neighbours, as (x,y) tuples, of the given space"""
        return {(x-1,y), (x+1,y), (x,y+1), (x,y-1)}.intersection(self.valid_spaces)

    def territory(self, x: int, y: int) -> Tuple[str, Set[Coords]]:
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
        if (x,y) not in self.valid_spaces:
            raise ValueError("Invalid coordinate")

        if self.get_space_content(x,y) != '':
            # designated space is a stone, not open territory
            return (NONE, set())

        checked = {(x,y)}
        terr = checked.copy()
        check_queue = self.get_neighbours(x,y)
        owners = set()
        while len(check_queue) > 0:
            space = check_queue.pop()
            space_cont = self.get_space_content(*space)
            if space_cont == NONE:
                check_queue.update(self.get_neighbours(*space) - checked)
                terr.add(space)
            else:
                owners.add(space_cont)
            checked.add(space)
        if len(owners) == 1:
            return (owners.pop(), terr)
        return (NONE, terr)


    def territories(self) -> Dict[str, Set[Coords]]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        terrs = {NONE: set(), WHITE: set(), BLACK: set()}
        unchecked = self.valid_spaces.copy()
        while len(unchecked) > 0:
            space = unchecked.pop()
            (owner, terr) = self.territory(*space)
            terrs[owner].update(terr)
            unchecked.difference_update(terr)
        return terrs
