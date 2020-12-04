import re


class Passport:
    def __init__(self, line: str):
        self.details = dict()
        entries = line.split(" ")
        for entry in entries:
            if entry:
                self.details[entry[:3]] = entry[4:]

    @property
    def is_valid(self):
        expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for key in expected_keys:
            if key not in self.details:
                return False
        return True

    @property
    def is_valid_strict(self):
        for key in self.details.keys():
            if not self.validate_value(key):
                return False
        return self.is_valid

    def validate_value(self, key):
        value = self.details[key]
        if key == "byr":
            return (len(value) == 4) & (int(value) >= 1920) & (int(value) <= 2002)
        elif key == "iyr":
            return (len(value) == 4) & (int(value) >= 2010) & (int(value) <= 2020)
        elif key == "eyr":
            return (len(value) == 4) & (int(value) >= 2020) & (int(value) <= 2030)
        elif key == "hgt":
            pattern = r"(\d+)(in|cm)"
            reg_exp = re.search(pattern, value)
            if reg_exp is None:
                return False
            number = int(reg_exp.group(1))
            unit = reg_exp.group(2)
            if unit == "cm":
                return (number >= 150) & (number <= 193)
            elif unit == "in":
                return (number >= 59) & (number <= 76)
            else:
                raise ValueError("Unknown unit")
        elif key == "hcl":
            pattern = re.compile(r"#([a-f]|\d){6}")
            return pattern.match(value)
        elif key == "ecl":
            pattern = re.compile(r"amb|blu|brn|gry|grn|hzl|oth")
            return pattern.match(value)
        elif key == "pid":
            pattern = re.compile(r"^\d{9}$")
            return pattern.match(value)
        elif key == "cid":
            return True
        else:
            raise ValueError(f"Unknown key: {key}")


def count_valid(passports, strict=False):
    if strict:
        return sum([p.is_valid_strict for p in passports])
    else:
        return sum([p.is_valid for p in passports])
