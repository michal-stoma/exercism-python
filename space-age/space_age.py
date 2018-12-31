class SpaceAge(object):
    def __init__(self, seconds):
        self.age = seconds
        self.reference = 31557600
        self.periods = {
            'earth': self.reference,
            'mercury': 0.2408467 * self.reference,
            'venus': 0.61519726 * self.reference,
            'mars': 1.8808158 * self.reference,
            'jupiter': 11.862615 * self.reference,
            'saturn': 29.447498 * self.reference,
            'uranus': 84.016846 * self.reference,
            'neptune': 164.79132 * self.reference
        }

        for _name in self.periods:
            _method_name = 'on_{}'.format(_name)
            setattr(self, _method_name, self._calc(_name))

    @property
    def seconds(self):
        return self.age

    def _calc(self, planet):
        return lambda: round(self.age / self.periods[planet], 2)
