import re


class Password:
    def __init__(self, line, old_policy=True):
        self.old_policy = old_policy
        pattern = r"(\d+)-(\d+) (\w): (.+)(?:\n?)"
        reg_exp = re.search(pattern, line)
        self.min = int(reg_exp.group(1))
        self.max = int(reg_exp.group(2))
        self.letter = reg_exp.group(3)
        self.password = reg_exp.group(4)

    @property
    def is_valid_sled_rental(self):
        count = self.password.count(self.letter)
        return (count >= self.min) & (count <= self.max)

    def is_valid(self, old_policy=True):
        if old_policy:
            count = self.password.count(self.letter)
            return (count >= self.min) & (count <= self.max)
        else:
            first_letter = self.password[self.min-1]
            second_letter = self.password[self.max-1]
            return (first_letter == self.letter) ^ (second_letter == self.letter)


def count_number_valid(passwords, old_policy=True):
    return sum([p.is_valid(old_policy) for p in passwords])
