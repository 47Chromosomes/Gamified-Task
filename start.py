"""
This file contains all the operations to run the game.
"""
import os
import sys
import time
from mechanics import *
quest = Quests()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F") # Move cursor up
        sys.stdout.write("\033[K") # Clear line content
    sys.stdout.flush()

print('STUDYQUEST INITIALIZING…')
print("A Gamified Task Prioritizer")
print(
		"1. Quest Log\n"
		"2. Add Quest\n"
		"3. Complete Quest\n"
		"4. Edit/Delete Quest\n"
		"5. View Stats\n"
		"6. Save & Exit\n"
)

while True:
    ch = input("Enter Command: ")

    if ch == '1':
        while True:
            ch2 = input(
                "[1] View Quests\n"
                "[2] View Sorted Quests by Deadline\n"
                "[3] View Sorted Quests by Difficulty\n"
                "[4] Back to Main Menu\n"
                "Enter Command: "
            )

            if ch2 == '1':
                clear_lines(5)
                quest.view_quests()
                time.sleep(2)
                clear_lines(len(quest.container))
            elif ch2 == '2':
                clear_lines(5)
                quest.sorting_deadline()
                time.sleep(2)
                clear_lines(len(quest.container))
            elif ch2 == '3':
                clear_lines(5)
                quest.sorting_difficulty()
                time.sleep(2)
                clear_lines(len(quest.container))
            elif ch2 == '4':
                clear_lines(5)
                time.sleep(2)
                break
            else:
                clear_lines(5)
                print("Invalid Choice... Try Again")
                time.sleep(2)
                clear_lines(1)
    elif ch == '2':
        name = input("Enter Quest Name: ")
        deadline = input("Enter Deadline (YYYY-MM-DD): ")
        difficulty = int(input("Enter Difficulty (1-10): "))
        quest.add_task(name, deadline, difficulty)
        
        time.sleep(3)
        clear_lines(4)
    elif ch == '3':
        pass

    elif ch == '4':
        pass

    elif ch == '5':
        pass
    
    elif ch == '6':
        print("Thank you for playing")
        break

    else:
        print("Invalid Option!... try again")

    input("Press [Enter] To Continue...")
    clear_lines(2)