class Matrix:
    def __init__(self, matrix_string):
        self.rows = [ [int(c) for c in r.split()]
                      for r in matrix_string.splitlines() ]

    def row(self, index):
        return self.rows[index-1].copy()

    def column(self, index):
        return [ r[index-1] for r in self.rows ]
