from aoc2020 import get_input
from aoc2020.d08_handheld_halting import AnswerD08, Instruction


def test_read_input():
    example = AnswerD08(get_input(__file__, "example1.txt")).input
    assert example.n_lines == 9

    assert example.lines[0].instruction == Instruction.NOP
    assert example.lines[0].value == 0
    assert example.lines[1].instruction == Instruction.ACC
    assert example.lines[1].value == 1
    assert example.lines[2].instruction == Instruction.JMP
    assert example.lines[2].value == 4
    assert example.lines[3].instruction == Instruction.ACC
    assert example.lines[3].value == 3
    assert example.lines[4].instruction == Instruction.JMP
    assert example.lines[4].value == -3
    assert example.lines[5].instruction == Instruction.ACC
    assert example.lines[5].value == -99
    assert example.lines[6].instruction == Instruction.ACC
    assert example.lines[6].value == 1
    assert example.lines[7].instruction == Instruction.JMP
    assert example.lines[7].value == -4
    assert example.lines[8].instruction == Instruction.ACC
    assert example.lines[8].value == 6


def test_answers():
    example = AnswerD08(get_input(__file__, "example1.txt"))
    assert example.answer1 == 5
    assert example.answer2 == 8

    input_ = AnswerD08(get_input(__file__, "input.txt"))
    assert input_.answer1 == 2034
    assert input_.answer2 == 672
