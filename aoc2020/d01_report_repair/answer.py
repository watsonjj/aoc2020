from aoc2020.answer import Answer
from aoc2020.d01_report_repair import sum_pair_equals, sum_triad_equals
import numpy as np


class AnswerD01(Answer):
    def _read_input(self, input_path):
        return np.loadtxt(input_path)

    @property
    def answer1(self):
        sum_pair = sum_pair_equals(self.input, desired_result=2020)
        return np.product(self.input[sum_pair])

    @property
    def answer2(self):
        sum_triad = sum_triad_equals(self.input, desired_result=2020)
        return np.product(self.input[sum_triad])
