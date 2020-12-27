from math import floor, ceil


class BoardingPass:
    def __init__(self, code):
        min_row = 0
        max_row = 127
        min_column = 0
        max_column = 7
        for char in code:
            mid_row = min_row + (max_row - min_row)/2
            mid_column = min_column + (max_column - min_column)/2
            if char == "F":
                max_row = floor(mid_row)
            elif char == "B":
                min_row = ceil(mid_row)
            elif char == "L":
                max_column = floor(mid_column)
            elif char == "R":
                min_column = ceil(mid_column)
            else:
                raise ValueError(f"Unknown char: {char}")
        if min_row != max_row:
            raise ValueError(f"Incomplete row selection: {min_row} - {max_row}")
        if min_column != max_column:
            raise ValueError(f"Incomplete column selection: {min_column} - {max_column}")

        self.row = min_row
        self.column = min_column

    @property
    def id(self):
        return self.row * 8 + self.column

    def __gt__(self, other):
        return self.id > other.id
