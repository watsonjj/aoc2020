from aoc2020 import get_example, get_input
from aoc2020.d03_toboggan_trajectory import AnswerD03, Slope
import numpy as np
import pytest


def test_read_input():
    example = AnswerD03(get_example(__file__))
    assert example.input.shape == (11, 11)
    assert example.input.dtype == bool


def test_slope():
    slope_map = np.array([[0, 0], [0, 1], [0, 1]], dtype=np.bool)
    slope = Slope(slope_map)
    assert not slope.tree_at_position
    assert slope.move(right=0, down=1)
    assert not slope.tree_at_position
    assert slope.move(right=1, down=0)
    assert slope.tree_at_position
    assert slope.move(right=2, down=0)
    assert slope.tree_at_position
    assert slope.move(right=2, down=1)
    assert slope.tree_at_position
    assert not slope.move(right=2, down=1)
    with pytest.raises(IndexError):
        _ = slope.tree_at_position

    slope.reset()
    assert slope.position == (0, 0)


def test_count_tree_until_bottom():
    slope_map = np.array([[0, 0], [0, 1], [0, 1]], dtype=np.bool)
    slope = Slope(slope_map)
    assert slope.count_tree_until_bottom(right=1, down=1) == 1
    assert slope.position == (0, 0)
    assert slope.count_tree_until_bottom(right=3, down=1) == 1
    assert slope.count_tree_until_bottom(right=3, down=3) == 0


def test_answers():
    example = AnswerD03(get_example(__file__))
    assert example.answer1 == 7
    assert example.answer2 == 336

    input_ = AnswerD03(get_input(__file__))
    assert input_.answer1 == 195
    assert input_.answer2 == 3772314000
