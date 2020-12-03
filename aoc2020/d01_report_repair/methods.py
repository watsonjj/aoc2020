import numpy as np


def sum_pair_equals(values, desired_result=2020):
    sum_ = values + values[:, None]
    return np.array(np.where(sum_ == desired_result))[:, 0]


def sum_triad_equals(values, desired_result=2020):
    sum_ = values + values[:, None] + values[:, None, None]
    return np.array(np.where(sum_ == desired_result))[:, 0]
