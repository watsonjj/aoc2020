from aoc2020.answer import Answer
from aoc2020.d08_handheld_halting import Code, Instruction


class AnswerD08(Answer):
    def _read_input(self, input_path):
        code = Code()
        with open(input_path) as r:
            for line in r:
                code.add_line(line.rstrip())
        return code

    @property
    def answer1(self):
        try:
            self.input.run()
        except ValueError:
            return self.input.accumulator
        raise ValueError("No infinite loop found :(")

    @property
    def answer2(self):
        for iline in range(self.input.n_lines):
            if self.input.lines[iline].instruction is Instruction.NOP:
                self.input.lines[iline].instruction = Instruction.JMP
                try:
                    self.input.run()
                except ValueError:
                    self.input.lines[iline].instruction = Instruction.NOP
                    continue
                return self.input.accumulator
            elif self.input.lines[iline].instruction is Instruction.JMP:
                self.input.lines[iline].instruction = Instruction.NOP
                try:
                    self.input.run()
                except ValueError:
                    self.input.lines[iline].instruction = Instruction.JMP
                    continue
                return self.input.accumulator
            else:
                continue
        raise ValueError("Unable to fix code")
