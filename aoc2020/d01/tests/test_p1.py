from aoc2020.d01.p1 import sum_pair_equals, sum_triad_equals, product_result, answer1, answer2, load_input1
import numpy as np
import pytest


@pytest.fixture(scope="module")
def example_values():
    return np.array([1721, 979, 366, 299, 675, 1456])


def test_sum_pair_equals(example_values):
    values = np.array([2, 5, 7])
    assert np.array_equal(sum_pair_equals(values, 7), [0, 1])

    assert np.array_equal(sum_pair_equals(example_values, 2020), [0, 3])


def test_sum_triad_equals(example_values):
    values = np.array([2, 5, 8, 13])
    assert np.array_equal(sum_triad_equals(values, 20), [0, 1, 3])

    assert np.array_equal(sum_triad_equals(example_values, 2020), [1, 2, 4])


def test_product_result(example_values):
    sum_pair = sum_pair_equals(example_values, 2020)
    assert product_result(example_values, sum_pair) == 514579


def test_answer1_example(example_values):
    assert answer1(example_values) == 514579


def test_answer2_example(example_values):
    assert answer2(example_values) == 241861950


def test_load_input1():
    assert load_input1().size > 1


def test_answer1():
    values = load_input1()
    assert answer1(values) == 913824


def test_answer2():
    values = load_input1()
    assert answer2(values) == 240889536
