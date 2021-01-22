from enum import Enum
from dataclasses import dataclass


class Instruction(Enum):
    NOP = 0
    ACC = 1
    JMP = 2


@dataclass
class Line:
    instruction: Instruction
    value: int


class Code:
    def __init__(self):
        self.lines = []
        self.accumulator = 0

    def add_line(self, line):
        instruction_str, value_str = line.split(" ")
        self.lines.append(Line(Instruction[instruction_str.upper()], int(value_str)))

    @property
    def n_lines(self):
        return len(self.lines)

    def run(self):
        current_line_index = 0
        lines_hit = set()
        self.accumulator = 0
        while current_line_index < self.n_lines:
            if current_line_index in lines_hit:
                raise ValueError("Infinite loop detected")
            lines_hit.add(current_line_index)

            line = self.lines[current_line_index]
            line_jmp = 1
            if line.instruction is Instruction.NOP:
                pass
            elif line.instruction is Instruction.ACC:
                self.accumulator += line.value
            elif line.instruction is Instruction.JMP:
                line_jmp = line.value
            else:
                raise ValueError("Unknown instruction")
            current_line_index += line_jmp
