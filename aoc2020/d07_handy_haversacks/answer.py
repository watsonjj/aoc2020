from aoc2020.answer import Answer
from aoc2020.d07_handy_haversacks import BagRules


class AnswerD07(Answer):
    def _read_input(self, input_path):
        bag_rules = BagRules()
        with open(input_path) as r:
            for line in r:
                bag_rules.add_rule(line.rstrip())
        return bag_rules

    @property
    def answer1(self):
        return len(set(self.input.bags_which_contain("shiny gold")))

    @property
    def answer2(self):
        return len(self.input.all_bags_inside("shiny gold"))
