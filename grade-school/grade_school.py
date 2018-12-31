class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = {}

    def grade(self, grade):
        return self.roster.get(grade, [])

    def add(self, student, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        self.roster[grade].append(student)

    def sort(self):
        for key, value in sorted(self.roster.items()):
            yield key, tuple(sorted(value))
