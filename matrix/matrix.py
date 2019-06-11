class Matrix(object):
    def __init__(self, matrix_string):
        # Create a matrix from a string: a list of lists.
        # Split the string on newline to get a list of strings
        # representing rows. Then every row gets splitted, and each
        # value of resulting lists is converted into int. Finally, a map
        # object gets converted back into list.
        self.matrix = [[int(element) for element in row.split()]
                       for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [row[index] for row in self.matrix]
