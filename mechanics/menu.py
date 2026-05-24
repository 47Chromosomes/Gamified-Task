"""
This FIle contains all menu options of the system
"""

import json
from .data_structure import Task_HashTable, stack, queue
from .utils import clear_lines, clear_screen, pause, box, line
from .system import Tasks_System


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
            "Difficulty Dominance (displays the hardest task to accomplish)\n"
            "Deadline Defense (shows the first most needed to accomplish)\n"
        )
        ch = input("What type of Mode would you like to do?: ")
        if ch.lower() in ["deadline", "deadline defense"]:
            tasks.sort_tasks("deadline")
            name = input("What task would you like to do?: ")
            if name in tasks:
                self.system.complete_task(name = name, mode = ch)
            else:
                return f"No {name} exists on the list"
        elif ch.lower() in ["difficulty", "difficulty dominance"]:
            tasks.sort_tasks("difficulty")
            name = input("What task would you like to do?: ")
            if name in tasks:
                self.system.complete_task(name = name, mode = ch)
            else:
                return f"No {name} exists on the list"
