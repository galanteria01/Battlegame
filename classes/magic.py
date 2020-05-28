import random
class Spell:                                             #Created spells to get player some special attacking powers
    def __init__(self,name,cost,dmg,type):
        self.name=name
        self.cost=cost
        self.dmg=dmg
        self.type=type

    def damage_generate(self):
        low=self.dmg-15
        high=self.dmg+15
        return random.randrange(low,high)


