from aoc2020 import get_input
from aoc2020.d06_custom_customs import AnswerD06


def test_read_input():
    example = AnswerD06(get_input(__file__, "example1.txt")).input
    assert len(example) == 5

    assert example[0].n_people == 1
    assert example[0].n_total_yes == 3
    assert example[0].n_unique_yes == 3

    assert example[1].n_people == 3
    assert example[1].n_total_yes == 3
    assert example[1].n_unique_yes == 3

    assert example[2].n_people == 2
    assert example[2].n_total_yes == 4
    assert example[2].n_unique_yes == 3

    assert example[3].n_people == 4
    assert example[3].n_total_yes == 4
    assert example[3].n_unique_yes == 1

    assert example[4].n_people == 1
    assert example[4].n_total_yes == 1
    assert example[4].n_unique_yes == 1


def test_answers():
    example = AnswerD06(get_input(__file__, "example1.txt"))
    assert example.answer1 == 11
    assert example.answer2 == 6

    input_ = AnswerD06(get_input(__file__, "input.txt"))
    assert input_.answer1 == 6504
    assert input_.answer2 == 3351
