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

            print(f"{name} added to Quest Log!")
        else:
            return f"{name} already in Quest Log!"


    def remove(self, name):
        if name in self.container:
            del self.container[name]
        else:
            return f"{name} not in Quest Log!"
        
    

    