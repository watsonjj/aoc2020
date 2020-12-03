from aoc2020 import get_example, get_input
from aoc2020.d01_report_repair import sum_pair_equals, sum_triad_equals, AnswerD01
import numpy as np


def test_sum_pair_equals():
    values = np.array([2, 5, 7])
    assert np.array_equal(sum_pair_equals(values, 7), [0, 1])

    values = np.array([1721, 979, 366, 299, 675, 1456])
    assert np.array_equal(sum_pair_equals(values, 2020), [0, 3])


def test_sum_triad_equals():
    values = np.array([2, 5, 8, 13])
    assert np.array_equal(sum_triad_equals(values, 20), [0, 1, 3])

    values = np.array([1721, 979, 366, 299, 675, 1456])
    assert np.array_equal(sum_triad_equals(values, 2020), [1, 2, 4])


def test_example_answer1():
    example = AnswerD01(get_example(__file__))
    assert example.answer1 == 514579


def test_example_answer2():
    example = AnswerD01(get_example(__file__))
    assert example.answer2 == 241861950


def test_answer1():
    input_ = AnswerD01(get_input(__file__))
    assert input_.answer1 == 913824


def test_answer2():
    input_ = AnswerD01(get_input(__file__))
    assert input_.answer2 == 240889536
