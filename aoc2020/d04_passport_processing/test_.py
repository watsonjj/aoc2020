from aoc2020 import get_input
from aoc2020.d04_passport_processing import AnswerD04, count_valid, Passport


def test_read_input():
    example = AnswerD04(get_input(__file__, "example1.txt")).input
    assert len(example) == 4

    assert example[0].details['byr'] == "1937"
    assert example[0].details['iyr'] == "2017"
    assert example[0].details['eyr'] == "2020"
    assert example[0].details['hgt'] == "183cm"
    assert example[0].details['hcl'] == "#fffffd"
    assert example[0].details['ecl'] == "gry"
    assert example[0].details['pid'] == "860033327"
    assert example[0].details['cid'] == "147"
    assert example[0].is_valid

    assert example[1].details['byr'] == "1929"
    assert example[1].details['iyr'] == "2013"
    assert example[1].details['eyr'] == "2023"
    assert example[1].details['hcl'] == "#cfa07d"
    assert example[1].details['ecl'] == "amb"
    assert example[1].details['pid'] == "028048884"
    assert example[1].details['cid'] == "350"
    assert not example[1].is_valid

    assert example[2].details['byr'] == "1931"
    assert example[2].details['iyr'] == "2013"
    assert example[2].details['eyr'] == "2024"
    assert example[2].details['hgt'] == "179cm"
    assert example[2].details['hcl'] == "#ae17e1"
    assert example[2].details['ecl'] == "brn"
    assert example[2].details['pid'] == "760753108"
    assert example[2].is_valid

    assert example[3].details['iyr'] == "2011"
    assert example[3].details['eyr'] == "2025"
    assert example[3].details['hgt'] == "59in"
    assert example[3].details['hcl'] == "#cfa07d"
    assert example[3].details['ecl'] == "brn"
    assert example[3].details['pid'] == "166559648"
    assert not example[3].is_valid


def test_count_valid():
    example = AnswerD04(get_input(__file__, "example1.txt")).input
    assert count_valid(example, strict=False) == 2
    example = AnswerD04(get_input(__file__, "example1.txt")).input
    assert count_valid(example, strict=True) == 2
    example = AnswerD04(get_input(__file__, "example2.txt")).input
    assert count_valid(example, strict=True) == 0
    example = AnswerD04(get_input(__file__, "example3.txt")).input
    assert count_valid(example, strict=True) == 4


def test_validate_key():
    assert Passport("byr:2002").validate_value('byr')
    assert not Passport("byr:2003").validate_value('byr')

    assert Passport("hgt:60in").validate_value('hgt')
    assert Passport("hgt:190cm").validate_value('hgt')
    assert not Passport("hgt:190in").validate_value('hgt')
    assert not Passport("hgt:190").validate_value('hgt')

    assert Passport("hcl:#123abc").validate_value('hcl')
    assert not Passport("hcl:#123abz").validate_value('hcl')
    assert not Passport("hcl:123abc").validate_value('hcl')

    assert Passport("ecl:brn").validate_value('ecl')
    assert not Passport("ecl:wat").validate_value('ecl')

    assert Passport("pid:000000001").validate_value('pid')
    assert not Passport("pid:0123456789").validate_value('pid')


def test_answers():
    example = AnswerD04(get_input(__file__, "example1.txt"))
    assert example.answer1 == 2
    example = AnswerD04(get_input(__file__, "example2.txt"))
    assert example.answer2 == 0
    example = AnswerD04(get_input(__file__, "example3.txt"))
    assert example.answer2 == 4

    input_ = AnswerD04(get_input(__file__, "input.txt"))
    assert input_.answer1 == 235
    assert input_.answer2 == 194
