class HighScores:
    def __init__(self, scores):
        self.scores = scores
        self.latest = lambda: scores[-1]
        self.personal_best = lambda: max(self.scores)
        self.personal_top_three = lambda: sorted(self.scores)[-1:-4:-1]
