"""Exercism -> gigasecond."""
from datetime import timedelta


def add_gigasecond(date):
    """Add 10^9 seconds to given date. Return datetime object."""
    return date + timedelta(seconds=10 ** 9)