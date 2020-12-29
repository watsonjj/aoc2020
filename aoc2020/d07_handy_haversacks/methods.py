import re


class BagRules:
    def __init__(self):
        self.rules = {}

    def add_rule(self, line):
        items = line.split(" bags contain ")
        container = items[0]

        inside_list = []
        if not "no other bags" in items[1]:
            all_inside = items[1].split(", ")
            pattern = re.compile(r"(\d+) (.+) bags?\.?")
            for inside in all_inside:
                regexr = re.match(pattern, inside)
                n_bags = int(regexr.group(1))
                bag_type = regexr.group(2)
                inside_list += [bag_type]*n_bags
        self.rules[container] = inside_list

    @property
    def n_rules(self):
        return len(self.rules)

    def bags_which_contain(self, bag_type):
        bags = []
        for container, contents in self.rules.items():
            if bag_type in contents:
                bags.append(container)
                bags.extend(self.bags_which_contain(container))
        return bags

    def all_bags_inside(self, bag_type):
        bags = []
        bags_directly_inside = self.rules[bag_type]
        for bag in bags_directly_inside:
            bags.extend(self.all_bags_inside(bag))
        return bags + bags_directly_inside
