from aoc2020 import get_example, get_input
from aoc2020.d02_password_philosophy import AnswerD02, Password, count_number_valid


def test_parse_input():
    password = Password("1-3 a: abcde")
    assert password.min == 1
    assert password.max == 3
    assert password.letter == 'a'
    assert password.password == "abcde"

    password = Password("1-3 b: cdefg")
    assert password.min == 1
    assert password.max == 3
    assert password.letter == 'b'
    assert password.password == "cdefg"

    password = Password("2-9 c: ccccccccc")
    assert password.min == 2
    assert password.max == 9
    assert password.letter == 'c'
    assert password.password == "ccccccccc"


def test_is_valid():
    password = Password("1-3 a: abcde")
    assert password.is_valid(old_policy=True)
    assert password.is_valid(old_policy=False)

    password = Password("1-3 b: cdefg")
    assert not password.is_valid(old_policy=True)
    assert not password.is_valid(old_policy=False)

    password = Password("2-9 c: ccccccccc")
    assert password.is_valid(old_policy=True)
    assert not password.is_valid(old_policy=False)


def test_count_number_valid_passwords():
    passwords = [
        Password("1-3 a: abcde"),
        Password("1-3 b: cdefg"),
        Password("2-9 c: ccccccccc")
    ]
    assert count_number_valid(passwords, old_policy=True) == 2
    assert count_number_valid(passwords, old_policy=False) == 1


def test_answers():
    example = AnswerD02(get_example(__file__))
    assert example.answer1 == 2
    assert example.answer2 == 1

    input_ = AnswerD02(get_input(__file__))
    assert input_.answer1 == 564
    assert input_.answer2 == 325
