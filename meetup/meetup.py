from datetime import date, timedelta


class MeetupDayException(Exception):
    pass


def _gen_days(year, month, weekday):
    d = date(year, month, 1)
    days = ()
    while d.month == month:
        if d.strftime('%A') == weekday:
            days += (d, )
        d += timedelta(days=1)
    return days


def meetup_day(year, month, weekday, count):
    try:
        if count == 'teenth':
            for x in _gen_days(year, month, weekday):
                if x.day in range(13, 20):
                    return x

        if count == 'last':
            idx = -1
        else:
            idx = int(count[0]) - 1
        return _gen_days(year, month, weekday)[idx]
    except:
        raise MeetupDayException