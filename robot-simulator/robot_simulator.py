NORTH, EAST, SOUTH, WEST = range(4)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self.bearing = bearing

    @property
    def coordinates(self):
        return (self._x, self._y)

    def advance(self):
        # We move across x coordinate, when facing EAST or WEST
        # and across y otherwise.
        # Depending on bearing, we have to make +1 (to NORTH and EAST)
        # or -1 step (to SOUTH and WEST).

        if self.bearing in [EAST, WEST]:
            self._x = self._x + EAST - self.bearing + 1
        else:
            self._y = self._y + NORTH - self.bearing + 1

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def simulate(self, orders):
        _dispatch = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }

        [_dispatch[_order]() for _order in orders]