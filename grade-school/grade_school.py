class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = {}

    def grade(self, grade):
        return self.roster.get(grade, set())

    def add(self, student, grade):
        self.roster.setdefault(grade, set()).add(student)

    def sort(self):
        return ((key, tuple(sorted(value))) for key, value
                in sorted(self.roster.items()))
