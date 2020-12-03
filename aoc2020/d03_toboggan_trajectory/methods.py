

class Slope:
    def __init__(self, slope_map, start=(0, 0)):
        self.slope_map = slope_map
        self._start = start
        self.position = start

    def move(self, right=3, down=1):
        n_rows, n_columns = self.slope_map.shape
        self.position = (
            (self.position[0] + down),
            (self.position[1] + right) % n_columns
        )
        return self.position[0] < n_rows

    def reset(self):
        self.position = self._start

    @property
    def tree_at_position(self) -> bool:
        return self.slope_map[self.position]

    def count_tree_until_bottom(self, right=3, down=1):
        n_trees = 0
        while self.move(right, down):
            if self.tree_at_position:
                n_trees += 1
        self.reset()
        return n_trees
