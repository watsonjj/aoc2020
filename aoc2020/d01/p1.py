import numpy as np
from pathlib import Path


def sum_pair_equals(values, desired_result=2020):
    sum_ = values + values[:, None]
    return np.array(np.where(sum_ == desired_result))[:, 0]


def sum_triad_equals(values, desired_result=2020):
    sum_ = values + values[:, None] + values[:, None, None]
    return np.array(np.where(sum_ == desired_result))[:, 0]


def product_result(values, sum_pair):
    return np.product(values[sum_pair])


def answer1(values):
    sum_pair = sum_pair_equals(values, 2020)
    return product_result(values, sum_pair)


def answer2(values):
    sum_triad = sum_triad_equals(values, 2020)
    return product_result(values, sum_triad)


def load_input1():
    return np.loadtxt(Path(__file__).parent / "input1.txt")
