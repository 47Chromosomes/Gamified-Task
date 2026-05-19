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
            return

        def parse_date(date_str):
            # Replaces spaces or slashes with dashes automatically
            clean_date = date_str.replace(" ", "-").replace("/", "-")
            return datetime.strptime(clean_date, "%Y-%m-%d")

        try:
            # Lambda fixed to correctly look inside the tuple details x[1]
            sorted_quests = sorted(self.container.items(), key=lambda x: parse_date(x[1]['Deadline']))
            for name, details in sorted_quests:
                print(f"Quest: {name}, Deadline: {details['Deadline']}, Difficulty: {details['Difficulty']}")
        except ValueError:
            print("Error: Could not read date format. Please use YYYY-MM-DD.")


    def sorting_difficulty(self):
        if not self.container:
            print("No quests in the log.")
            return # Stops execution so it doesn't crash below
            
        def parse_date(date_str):
            # Replaces spaces or slashes with dashes automatically
            clean_date = date_str.replace(" ", "-").replace("/", "-")
            return datetime.strptime(clean_date, "%Y-%m-%d")
        
        try:
            sorted_quests = sorted(self.container.items(), key=lambda x: parse_date(x[1]['Deadline']))
            for name, details in sorted_quests:
                print(f"Quest: {name}, Deadline: {details['Deadline']}, Difficulty: {details['Difficulty']}")
        except ValueError:
            print("Error: Difficulty must be an integer between 1 and 10.")




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
        
    

    