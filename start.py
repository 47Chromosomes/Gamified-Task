"""
This file contains all the operations to run the game.
"""
from mechanics.menu import Main_Menu
from mechanics.utils import clear_lines, clear_screen, pause

menu = Main_Menu()
Tasksys = menu.system

while True:
    menu.display_menu()
    choice = input("Enter your choice: ")

    #Finished
    if choice == "1":
        menu.QuestLog(Tasksys.Tasks)
        pause()
        
    #Finished
    elif choice == "2":
        menu.adda_task()

    elif choice == "3":
        menu.complete_task(Tasksys.Tasks)

    elif choice == "4":
        name = menu.delet_edit(Tasksys.Tasks)
        Tasksys.edit_delete_task(name)

    elif choice == "5":
        menu.profile()

    elif choice == "6":
        Tasksys.save_player()
        print("Task Saved Succesfully!")

    elif choice == "7":
        print("Thank you for Study Quest!")
        print("See you Soon! 👋")
        pause()
        break

    else:
        print("Invalid choice. Please try again.")
        pause(1)
        clear_lines(1)

    input("Press [ENTER] to Continue...")
    clear_lines(2)
    clear_screen()