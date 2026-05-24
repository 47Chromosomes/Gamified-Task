"""
This file Contains the player profile
"""

class Player:
    def __init__(self, name, level, exp = 0):
        self.name = name
        self.level = level
        self.exp = exp
        
    def gain_exp(self, amount):
        self.exp += amount
        print(f"Task Completed! Gained Amount is {amount}")
        self.check_level_up()

    def check_level_up(self):
        # Simple level-up logic: every 100 exp points, level up
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} leveled up to level {self.level}!")

    def __str__(self):
        #needs designing
        return f"Player: {self.name}, Level: {self.level}, EXP: {self.exp}"