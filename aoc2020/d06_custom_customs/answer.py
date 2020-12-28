from aoc2020.answer import Answer
from aoc2020.d06_custom_customs import GroupAnswers
import numpy as np


class AnswerD06(Answer):
    def _read_input(self, input_path):
        group_answers = [GroupAnswers()]
        with open(input_path) as r:
            for line in r:
                line = line.rstrip()
                if len(line) > 0:
                    group_answers[-1].add_persons_answers(line)
                else:
                    group_answers.append(GroupAnswers())
        return group_answers

    @property
    def answer1(self):
        return sum(group_answers.n_unique_yes for group_answers in self.input)

    @property
    def answer2(self):
        return sum(group_answers.n_common_yes for group_answers in self.input)
