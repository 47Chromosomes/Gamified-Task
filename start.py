"""
This file contains all the operations to run the game.
"""
import os
import sys
import time
from mechanics.data_structure import Quests

quest = Quests()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    sys.stdout.flush()

def pause():
    input("\nPress [Enter] To Continue...")

clear_screen()
print('STUDYQUEST INITIALIZING…')
print("A Gamified Task Prioritizer")

while True:
    print(
        "\n1. Quest Log"
        "\n2. Add Quest"
        "\n3. Complete Quest"
        "\n4. Edit/Delete Quest"
        "\n5. View Stats"
        "\n6. Save & Exit\n"
    )

    ch = input("Enter Command: ")

    if ch == '1':
        while True:
            ch2 = input(
                "\n[1] View Quests"
                "\n[2] View Sorted by Deadline"
                "\n[3] View Sorted by Difficulty"
                "\n[4] Back\n"
                "Enter Command: "
            )

            if ch2 == '1':
                clear_screen()
                quest.view_quests()
                pause()

            elif ch2 == '2':
                clear_screen()
                quest.sorting_deadline()
                pause()

            elif ch2 == '3':
                clear_screen()
                quest.sorting_difficulty()
                pause()

            elif ch2 == '4':
                clear_screen()
                break

            else:
                print("Invalid choice.")
                pause()

    elif ch == '2':
        clear_screen()

        name = input("Enter Quest Name: ")
        deadline = input("Enter Deadline (YYYY-MM-DD): ")

        difficulty = input("Enter Difficulty (1-10): ")

        quest.add_task(name, deadline, difficulty)

        pause()
        clear_screen()

    elif ch == '3':
        print("Complete Quest feature coming soon.")
        pause()

    elif ch == '4':
        print("Edit/Delete feature coming soon.")
        pause()

    elif ch == '5':
        print("Stats feature coming soon.")
        pause()

    elif ch == '6':
        print("Thank you for playing StudyQuest!")
        break

    else:
        print("Invalid Option!")
        pause()
