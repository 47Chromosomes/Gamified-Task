"""
This FIle is for the Data Structure that the system will use
"""
from datetime import datetime


#Arrays
class Quests:
    def __init__(self):
        self.status = "unfinished"
        self.container = {}

    def view_quests(self):
        if not self.container:
            print("No quests in the log.")
        else:
            for name, details in self.container.items():
                print(f"Quest: {name}, Deadline: {details['Deadline']}, Difficulty: {details['Difficulty']}")

    def sorting_deadline(self):
        if not self.container:
            print("No quests in the log.")
        else:
            sorted_quests = sorted(self.container.items(), key=lambda x: datetime.strptime(x[1]['Deadline'], "%Y-%m-%d"))
            for name, details in sorted_quests:
                print(f"Quest: {name}, Deadline: {details['Deadline']}, Difficulty: {details['Difficulty']}")

    def sorting_difficulty(self):
        if not self.container:
            print("No quests in the log.")
        else:
            sorted_quests = sorted(self.container.items(), key=lambda x: x[1]['Difficulty'], reverse=True)
            for name, details in sorted_quests:
                print(f"Quest: {name}, Deadline: {details['Deadline']}, Difficulty: {details['Difficulty']}")



    def add_task(self, name, deadline, difficulty):
        if name not in self.container:
            self.container[name] = {"Deadline": deadline, "Difficulty": difficulty}

            print(f"{name} added to Quest Log!")
        else:
            return f"{name} already in Quest Log!"


    def remove(self, name):
        if name in self.container:
            del self.container[name]
        else:
            return f"{name} not in Quest Log!"
        
    

    