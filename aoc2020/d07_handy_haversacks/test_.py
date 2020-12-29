from aoc2020 import get_input
from aoc2020.d07_handy_haversacks import AnswerD07


def test_read_input():
    example = AnswerD07(get_input(__file__, "example1.txt")).input
    assert example.n_rules == 9

    assert example.rules["light red"] == ["bright white"] + ["muted yellow"]*2
    assert example.rules["dark orange"] == ["bright white"]*3 + ["muted yellow"]*4
    assert example.rules["bright white"] == ["shiny gold"]
    assert example.rules["muted yellow"] == ["shiny gold"]*2 +["faded blue"]*9
    assert example.rules["shiny gold"] == ["dark olive"] + ["vibrant plum"]*2
    assert example.rules["dark olive"] == ["faded blue"]*3 + ["dotted black"]*4
    assert example.rules["vibrant plum"] == ["faded blue"]*5 + ["dotted black"]*6
    assert example.rules["faded blue"] == []
    assert example.rules["dotted black"] == []


def test_answers():
    example = AnswerD07(get_input(__file__, "example1.txt"))
    assert example.answer1 == 4
    assert example.answer2 == 32

    example = AnswerD07(get_input(__file__, "example2.txt"))
    assert example.answer2 == 126

    input_ = AnswerD07(get_input(__file__, "input.txt"))
    assert input_.answer1 == 124
    assert input_.answer2 == 34862
