"""
This file contains all the operations to run the game.
"""

from mechanics import *

quest = Quests()


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
ch = input("Enter Command: ")

if ch == '2':
    name = input("Enter Quest Name: ")
    deadline = input("Enter Deadline (YYYY-MM-DD): ")
    difficulty = int(input("Enter Difficulty (1-10): "))
    quest.add_task(name, deadline, difficulty)