from aoc2020.answer import Answer
from aoc2020.d04_passport_processing import Passport, count_valid


class AnswerD04(Answer):
    def _read_input(self, input_path):
        passports = []
        with open(input_path) as r:
            current_line = ""
            for line in r:
                line = line.rstrip()
                if len(line) > 0:
                    current_line += " " + line
                else:
                    passports.append(Passport(current_line))
                    current_line = ""
            passports.append(Passport(current_line))
        return passports

    @property
    def answer1(self):
        return count_valid(self.input, strict=False)

    @property
    def answer2(self):
        return count_valid(self.input, strict=True)
