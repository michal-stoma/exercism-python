class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        _latest = self.scores[-1]
        return _latest

    def personal_best(self):
        _best = max(self.scores)
        return _best

    def personal_top(self):
        _length = len(self.scores)
        _sorted_scores = sorted(self.scores, reverse=True)

        if _length <= 3:
            _result = _sorted_scores

        else:
            _result = _sorted_scores[0:3]

        return _result

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
