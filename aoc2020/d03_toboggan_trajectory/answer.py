from aoc2020.answer import Answer
from aoc2020.d03_toboggan_trajectory import Slope
import numpy as np


class AnswerD03(Answer):
    def _read_input(self, input_path):
        rows = []
        with open(input_path) as r:
            for line in r:
                rows.append(np.array(list(line.rstrip())))
        array = np.column_stack(rows).T
        return array == '#'

    @property
    def answer1(self):
        slope = Slope(self.input)
        return slope.count_tree_until_bottom(right=3, down=1)

    @property
    def answer2(self):
        slope = Slope(self.input)
        return np.product([
            slope.count_tree_until_bottom(right=1, down=1),
            slope.count_tree_until_bottom(right=3, down=1),
            slope.count_tree_until_bottom(right=5, down=1),
            slope.count_tree_until_bottom(right=7, down=1),
            slope.count_tree_until_bottom(right=1, down=2),
        ])
