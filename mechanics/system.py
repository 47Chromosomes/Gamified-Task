"""
This module contains the core mechanics of the project
"""
import json
import os
from datetime import datetime
from random import randint

from .player import Player
from .data_structure import stack, queue, Task_HashTable
from .utils import *


DATA_FILE = "player_data.json"
class Tasks_System:
    def __init__(self):
        self.player = None
        self.Tasks = Task_HashTable()
        self.load_data()
        self.difficulty_ranges = {
            "1": (5, 10),   # Easy
            "2": (10, 15),  # Medium
            "3": (15, 25),  # Hard
            "4": (25, 40)   # Boss
        }


        # Only greet if a player was loaded from file
        if self.player is not None:
            print(f"Welcome back {self.player.name}...👋")
            pause()
            clear_screen()



    #============================
    #INITIALIZING THE PLAYER's DATA
    #============================
    def create_player(self, name):
        self.player = Player(name, level=1)  
        # print(self.player.__str__())
        print(f"Welcome {self.player.name}!")
        pause()
        clear_screen()
        self.save_player()


    # =====================================================
    # SAVE / LOAD
    # =====================================================
    def save_player(self):
        data = {
            "player": {
                "name": self.player.name,
                "level": self.player.level,
                "exp": self.player.exp
            },
            "tasks": self.Tasks.to_dict()
        }

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        # Restore player
        if "player" in data:
            p = data["player"]
            self.player = Player(p["name"], p["level"], p["exp"])

        # Restore tasks
        if "tasks" in data:
            for key, value in data["tasks"].items():
                # Deadline back to datetime if needed
                deadline = value.get("Deadline")
                if isinstance(deadline, str):
                    try:
                        deadline = datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        pass
                value["Deadline"] = deadline
                self.Tasks[key] = value

                
    #============================
    #TOOLS FOR TASK MANAGEMENT
    #============================
    def add_task(self, name, difficulty, deadline_str):
        deadline = self.parse_deadline(deadline_str)
        if deadline is None:
            return f"Invalid deadline format: {deadline_str}. Use YYYY-MM-DD."

        # Store as string, not datetime
        deadline_str = deadline.strftime("%Y-%m-%d")
        self.Tasks[name] = {
            "Name": name,
            "Difficulty": difficulty,
            "Deadline": deadline_str
        }
        
        return (f"Task '{name}' added successfully!")
    
    def parse_deadline(self, deadline_str):
        try:
            if "-" in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            elif " " in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y %m %d")
            elif "/" in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y/%m/%d")
            elif "." in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y.%m.%d")
            elif "," in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y,%m,%d")
            elif "|" in deadline_str:
                deadline = datetime.strptime(deadline_str, "%Y|%m|%d")
            else:
                raise ValueError("Invalid date format")
            return deadline
        except ValueError:
            # Instead of returning a string, raise or return None
            return None

    def complete_task(self, name, mode="deadline", filename="player_data.json"):
        # Convert hash table to dict for sorting
        tasks_dict = self.Tasks.to_dict()

        if not tasks_dict:
            print("No tasks to complete.")
            return None

        # Choose sorting mode
        if mode == "difficulty":
            # Sort by difficulty (highest first)
            sorted_tasks = sorted(
                tasks_dict.values(),
                key=lambda t: int(t["Difficulty"]),  # ensure numeric
                reverse=True
            )
        elif mode == "deadline":
            # Sort by deadline (earliest first)
            sorted_tasks = sorted(
                tasks_dict.values(),
                key=lambda t: (
                    t["Deadline"] if isinstance(t["Deadline"], datetime)
                    else datetime.strptime(t["Deadline"], "%Y-%m-%d")
                )
            )
        else:
            print("Invalid mode selected.")
            return None

        # Find the task by name inside the sorted list
        task = next((t for t in sorted_tasks if t["Name"] == name), None)
        if not task:
            print(f"No task named {name} found.")
            return None

        # Remove from hash table
        task_name = task["Name"]
        del self.Tasks[task_name]

        # Award EXP based on difficulty range
        low, high = self.difficulty_ranges.get(str(task["Difficulty"]), (5, 10))
        gained_exp = randint(low, high)
        self.player.gain_exp(gained_exp)
        print(f"Completed task: {task_name} (+{gained_exp} EXP)")


        # Update JSON file (merge, don’t overwrite player info)
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # Normalize deadlines before saving (convert datetime → string)
        tasks_dict = self.Tasks.to_dict()
        for key, value in tasks_dict.items():
            deadline = value.get("Deadline")
            if isinstance(deadline, datetime):
                value["Deadline"] = deadline.strftime("%Y-%m-%d")
        data["tasks"] = tasks_dict

        #This just adds the completed tas to history
        if "completed_tasks" not in data:
            data["completed_tasks"] = []

        data["completed_tasks"].append({
            "Name": task["Name"],
            "Difficulty": task["Difficulty"],
            "Deadline": task["Deadline"]
        })

        # Then, Update player stats
        data["player"] = {
            "name": self.player.name,
            "level": self.player.level,
            "exp": self.player.exp
        }

        #After all that shinanegans, save it all to json file 
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"🎊🎉Congratulations player! Keep going!🎊🎉")
        return task


    #=================================
    #To delete or edit a Task
    #=================================
    def edit_delete_task(self, name, filename="player_data.json"):
        # Convert hash table to dict
        tasks_dict = self.Tasks.to_dict()

        if name not in tasks_dict:
            print(f"No task named {name} found.")
            return None

        task = tasks_dict[name]
        print(f"Selected task: {task['Name']} (Difficulty {task['Difficulty']}, Deadline {task['Deadline']})")

        action = input("Do you want to [edit] or [delete] this task? ").lower()

        if action == "delete":
            # Remove task
            del self.Tasks[name]
            print(f"Deleted task: {name}")

        elif action == "edit":
            # Allow editing difficulty and deadline
            new_difficulty = input("Enter new difficulty (leave blank to keep current): ")
            new_deadline = input("Enter new deadline (YYYY-MM-DD, leave blank to keep current): ")

            if new_difficulty.strip():
                task["Difficulty"] = new_difficulty
            if new_deadline.strip():
                try:
                    datetime.strptime(new_deadline, "%Y-%m-%d")  # validate format
                    task["Deadline"] = new_deadline
                except ValueError:
                    print("Invalid deadline format. Keeping old deadline.")

            # Update hash table
            self.Tasks[name] = task
            print(f"Edited task: {name}")

        else:
            print("Invalid action.")
            return None

        # Update JSON file
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Normalize deadlines before saving
        tasks_dict = self.Tasks.to_dict()
        for key, value in tasks_dict.items():
            deadline = value.get("Deadline")
            if isinstance(deadline, datetime):
                value["Deadline"] = deadline.strftime("%Y-%m-%d")

        data["tasks"] = tasks_dict

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        return task





# system = Tasks_System()
# system.add_task("Math", 4, "2024-06-30")
# system.load_player()
