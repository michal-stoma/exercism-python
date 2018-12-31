class Allergies(object):
    ALLERGENS = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats',
    }

    def __init__(self, score):
        self._score = score

        self.lst = [self.ALLERGENS[2 ** i] for
                    i in range(len(self.ALLERGENS)) if
                    self._score & (1 << i) != 0]

    def is_allergic_to(self, query):
        return True if query in self.lst else False