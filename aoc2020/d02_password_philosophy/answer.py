from aoc2020.answer import Answer
from aoc2020.d02_password_philosophy import Password, count_number_valid
import numpy as np


class AnswerD02(Answer):
    def _read_input(self, input_path):
        passwords = []
        with open(input_path) as r:
            for line in r:
                passwords.append(Password(line))
        return passwords

    @property
    def answer1(self):
        return count_number_valid(self.input, old_policy=True)

    @property
    def answer2(self):
        return count_number_valid(self.input, old_policy=False)
