class Queen:
    def __init__(self, row, column):
        if row <0: raise ValueError("row not positive")
        if column <0: raise ValueError("column not positive")
        if column >7: raise ValueError("column not on board")
        if row >7: raise ValueError("row not on board")
        self.row, self.column = row, column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column: raise ValueError("Invalid queen position: both queens in the same square")
        if self.column == another_queen.column or self.row == another_queen.row: return True
        if abs(self.column-another_queen.column)==abs(another_queen.row-self.row): return True #same diagonal
        return False
