from aoc2020.answer import Answer
from aoc2020.d05_binary_boarding import BoardingPass
import numpy as np


class AnswerD05(Answer):
    def _read_input(self, input_path):
        boarding_passes = []
        with open(input_path) as r:
            for line in r:
                line = line.rstrip()
                boarding_passes.append(BoardingPass(line))
        return boarding_passes

    @property
    def answer1(self):
        return max(self.input).id

    @property
    def answer2(self):
        ids = np.zeros(len(self.input))
        for i, boarding_pass in enumerate(self.input):
            ids[i] = boarding_pass.id

        ids = np.sort(ids)
        idx = np.where(np.diff(ids) == 2)[0][0]
        return ids[idx] + 1
