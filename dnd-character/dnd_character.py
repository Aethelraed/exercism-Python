from random import randint


class Character:
    def __init__(self):
        self.ability = lambda: randint(3, 18)
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)


def modifier(value):
    return (value - 10) // 2
