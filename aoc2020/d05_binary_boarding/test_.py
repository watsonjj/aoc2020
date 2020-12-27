from aoc2020 import get_input
from aoc2020.d05_binary_boarding import AnswerD05


def test_read_input():
    example = AnswerD05(get_input(__file__, "example1.txt")).input
    assert len(example) == 4

    assert example[0].row == 44
    assert example[0].column == 5
    assert example[0].id == 357

    assert example[1].row == 70
    assert example[1].column == 7
    assert example[1].id == 567

    assert example[2].row == 14
    assert example[2].column == 7
    assert example[2].id == 119

    assert example[3].row == 102
    assert example[3].column == 4
    assert example[3].id == 820


def test_answers():
    example = AnswerD05(get_input(__file__, "example1.txt"))
    assert example.answer1 == 820

    input_ = AnswerD05(get_input(__file__, "input.txt"))
    assert input_.answer1 == 980
    assert input_.answer2 == 607
