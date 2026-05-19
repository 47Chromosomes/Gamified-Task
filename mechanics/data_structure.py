"""
This FIle is for the Data Structure that the system will use
"""
from datetime import datetime


#Arrays
class Quests:
    def __init__(self, name, deadline, difficulty : int):
        self.name = name
        self._deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self._difficulty = difficulty 
        self.status = "unfinished"
        self.container = {}

    def add_tast(self, name, deadline, difficulty):
        if name not in self.container:
            self.container[name] = {"Deadline : ": deadline, "Difficulty": difficulty}

    def remove(self, name):
        if name in self.container:
            self.container.remove(name)
        else:
            return f"{name} not in {self.container}"
        
    

    