

class GroupAnswers:
    def __init__(self):
        self.members_answers = []

    def add_persons_answers(self, answers):
        self.members_answers.append(answers)

    @property
    def n_people(self):
        return len(self.members_answers)

    @property
    def n_total_yes(self):
        return len(''.join(self.members_answers))

    @property
    def n_unique_yes(self):
        return len(set(''.join(self.members_answers)))

    @property
    def n_common_yes(self):
        return len(set.intersection(*[set(a) for a in self.members_answers]))
