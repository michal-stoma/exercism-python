"""Exercism -> clock."""


class Clock(object):
    """Class representing a clock object."""

    def __init__(self, hours, minutes):
        """Construct a Clock() instance.

        Parameters:
            hour (integer) number of hours to be added / substracted
                from base time (00:00)
            minute - number of minutes to be added / substracted from
                base time (00:00)

        Given values are converted into time represented in minutes.
        """
        self._tm = (0 + hours) % 24 * 60
        self._tm += minutes

    def __str__(self):
        """Convert time back to hh:mm format and return it as a string."""
        self._h = self._tm // 60 % 24
        self._m = self._tm % 60
        return '{:02d}:{:02d}'.format(self._h, self._m)

    def __eq__(self, other):
        """Comparison of two instances by their string representation."""
        return str(self) == str(other)

    def add(self, minutes):
        """Add given number of minutes to Clock(). Return object."""
        self._tm += minutes
        return self