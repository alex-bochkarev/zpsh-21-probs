import numpy as np

class dice:
    def __init__(self):
        self.Omega = [face for face in '⚀⚁⚂⚃⚄⚅']

    def roll(self):
        return np.random.choice(self.Omega)


class coin:
    def __init__(self):
        self.Omega = ["H", "T"]

    def toss(self):
        return np.random.choice(self.Omega)
