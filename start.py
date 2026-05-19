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
                quest.view_quests()
            elif ch2 == '2':
                quest.sorting_deadline()
            elif ch2 == '3':
                quest.sorting_difficulty()
            elif ch2 == '4':
                break
            else:
                print("Invalid Choice... Try Again")

    elif ch == '2':
        name = input("Enter Quest Name: ")
        deadline = input("Enter Deadline (YYYY-MM-DD): ")
        difficulty = int(input("Enter Difficulty (1-10): "))
        quest.add_task(name, deadline, difficulty)
    
    elif ch == '3':
        pass

    elif ch == '4':
        pass

    elif ch == '5':
        pass
    
    elif ch == '6':
        pass

    else:
        print("Invalid Option!... try again")