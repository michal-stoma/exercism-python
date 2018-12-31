CHILDREN = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
PLANTS = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}


class Garden(object):
    def __init__(self, diagram, students=CHILDREN):
        self.students = students
        self.diagram = diagram.split()

    def plants(self, student):
        _index = self.students.index(student)
        _start = _index * 2
        _stop = _start + 2

        _result = [PLANTS[i[j]] for i in self.diagram
                   for j in range(_start, _stop)]

        return _result