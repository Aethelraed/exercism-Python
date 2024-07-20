"""
Schrödinger's Robot Naming
Please add some meaningful tests that truly reflect the instructions
"""

from random import randint


class Robot:
    def __init__(self):
        self.name = "AA00" + str(randint(0, 9))

    def reset(self):
        self.name = "AA001"
