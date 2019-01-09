class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        _latest = self.latest()
        _personal_best = self.personal_best()
        _difference = None

        if _latest == _personal_best:
            _msg = 'Your latest score was {latest}. That\'s your personal best!'

        else:
            _difference = _personal_best - _latest
            _msg = 'Your latest score was {latest}. That\'s {difference} short of your personal best!'

        _msg = _msg.format(latest=_latest, difference=_difference)

        return _msg
