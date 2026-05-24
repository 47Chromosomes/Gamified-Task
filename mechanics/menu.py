"""
Add a Description here
"""

import json
from .data_structure import Task_HashTable, stack, queue
from .utils import clear_lines, clear_screen, pause, box, line
from .system import Tasks_System
from datetime import datetime


class Main_Menu:
    def __init__(self):
        self.intro_screen()
        self.system = Tasks_System()
        self.menu_options = {
            "1": "Quest Log",
            "2": "Add Task",
            "3": "Complete Task",
            "4": "Edit/Delete Task",
            "5": "View Player Stats",
            "6": "Save Tasks",
            "7": "Exit"
        }
        self.difficulty_rate = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard",
            "4": "Boss"
        }
        # If no player loaded, create one
        if self.system.player is None:
            name = self.char_creation()
            self.system.create_player(name)

        
    def intro_screen(self):
        box("STUDYQUEST INITIALIZING...", "A Gamified Task Prioritizer")
        pause()
        clear_screen()

    def char_creation(self):
        box("CHARACTER CREATION")
        return input("Enter your character's name: ")
    
    
    def display_menu(self):
        box("MAIN MENU")
        for key, value in self.menu_options.items():
            print(f"{key}. {value}")
    
    def QuestLog(self, tasks):
        clear_screen()
        box("QUEST LOG")
        tasks.display()
        line()
        while True:
            print("[exit] to go back")
            ch = input("[sort] to sort the quest: ")

            if ch.lower() == "exit":
                return
            elif ch.lower() == "sort":
                clear_lines(1)
                while True:
                    sort = input("[Deadline] to sort by Deadline, [Difficulty] To sort by Difficulty: ")
                    if sort.lower() == "deadline":
                        clear_lines(3 + len(tasks.to_dict()))
                        tasks.sort_tasks(sort)
                        line()
                        break
                    elif sort.lower() == "difficulty":
                        clear_lines(3 + len(tasks.to_dict()))
                        tasks.sort_tasks(sort)
                        line()
                        break
                    elif sort.lower() == "exit":
                        return
                    else:
                        print("Invalid Option.. Try again")
                        pause(1)
                        clear_lines(2)
            else:
                print("Invalid Option.. Try again")
                pause(1)
                clear_lines(3)


    def profile(self, player_file="player_data.json"):
        clear_screen()
        box("Profile")

        with open(player_file, "r") as f:
            data = json.load(f)

        # Player info
        player = data.get("player", {})
        print(
            f"Name  : {player.get('name', 'Unknown')}\n"
            f"Level : {player.get('level', 'N/A')}\n"
            f"EXP   : {player.get('exp', 'N/A')}\n"
        )

        # Completed Quests
        print("Completed Quests:")
        completed = data.get("completed_tasks", [])
        if completed:
            for quest in completed:
                print(
                    f"- {quest.get('Name', 'Unknown')} "
                    f"(Difficulty: {quest.get('Difficulty', 'N/A')}, "
                    f"Deadline: {quest.get('Deadline', 'N/A')})"
                )
        else:
            print("No quests completed yet.")
        #Just for a new line
        print()
        ch = input("Do you want to empty the completed tasks? (Y/N): ")
        if ch.lower() in ['y', 'yes']:
            data["completed_tasks"] = []  # reset the list
            with open(player_file, "w") as f:
                json.dump(data, f, indent=4)
            print("All completed quests have been Emptied.")
        else:
            return


    #===========================
    #Adding a Task
    #===========================
    def adda_task(self):
        clear_screen()
        box("TASK INSERTING")
        print("[exit] to go back.")
        while True:
            subject = input("Enter subject: ")
            if subject.lower() == "exit":
                return
            for am,dif in self.difficulty_rate.items():
                print(f"{am} - {dif}")

            difficulty = input("Enter difficulty: ")
            deadline = input("Enter Deadline (Strictly YYYY-MM-DD): ")
            pause()
            print(self.system.add_task(subject, difficulty, deadline))
            pause(3)
            clear_lines(8)

    def delet_edit(self,tasks):
        clear_screen()
        box("DELETING/EDITING TASKS")
        tasks.display()
        line()
        name = input("Enter the task name to edit or delete: ")
        return name


    #================================
    #This just shows how the implementation of stack and queues
    #================================
    def complete_task(self, tasks):
        clear_screen()
        box("Completing Task")
        print(
            "Normal Mode → choose a task by name\n"
            "Difficulty Dominance → hardest task first (Stack)\n"
            "Deadline Defense → earliest deadline first (Queue)\n"
        )
        ch = input("What type of Mode would you like to do?: ")

        tasks_dict = tasks.to_dict()

        if not tasks_dict:
            print("No tasks available.")
            return

        # Difficulty Dominance (Stack)
        if ch.lower() in ["difficulty", "difficulty dominance"]:
            s = stack()
            for t in sorted(tasks_dict.values(), key=lambda t: int(t["Difficulty"])):
                s.push(t)
            task = s.pop()
            print(f"\nNext hardest task: {task['Name']} (Difficulty: {task['Difficulty']}, Deadline: {task['Deadline']})")
            confirm = input(f"Do you want to complete '{task['Name']}'? (y/n): ")
            if confirm.lower() == "y":
                self.system.complete_task(name=task["Name"], mode="difficulty")
            else:
                print("Returning to main menu...")

        # Deadline Defense (Queue)
        elif ch.lower() in ["deadline", "deadline defense"]:
            q = queue()
            for t in sorted(
                tasks_dict.values(),
                key=lambda t: (
                    t["Deadline"] if isinstance(t["Deadline"], datetime)
                    else datetime.strptime(t["Deadline"], "%Y-%m-%d")
                )
            ):
                q.enqueue(t)
            task = q.dequeue()
            print(f"\nNext earliest deadline task: {task['Name']} (Difficulty: {task['Difficulty']}, Deadline: {task['Deadline']})")
            confirm = input(f"Do you want to complete '{task['Name']}'? (y/n): ")
            if confirm.lower() == "y":
                self.system.complete_task(name=task["Name"], mode="deadline")
            else:
                print("Returning to main menu...")

        # Normal Mode
        elif ch.lower() in ["normal", "normal mode"]:
            print("\nAvailable Tasks:")
            for t in tasks_dict.values():
                deadline = (
                    t["Deadline"].strftime("%Y-%m-%d")
                    if isinstance(t["Deadline"], datetime)
                    else str(t["Deadline"])
                )
                print(f"- {t['Name']} (Difficulty: {t['Difficulty']}, Deadline: {deadline})")

            name = input("\nEnter the name of the task you want to complete: ")
            task = tasks_dict.get(name)

            if not task:
                print(f"No task named {name} found.")
                return

            confirm = input(f"Are you sure you want to complete '{name}'? (y/n): ")
            if confirm.lower() == "y":
                self.system.complete_task(name=name, mode="normal")
            else:
                print("Returning to main menu...")

        else:
            print(f"Invalid mode: {ch}")


