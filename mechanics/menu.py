"""
Add a Description here
"""
# YOU'RE FREE TO EDIT ANY PARTS HERE
import os
import sys
import time
from mechanics.data_structure import Quests

quest_log = Quests()

player_profile = {
    "Level": 1,
    "XP": 0,
    "Streak": 0,
    "Completed_Quests": []
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    while True:
        clear_screen()
        print("=========================================")
        print("         STUDYQUEST INITIALIZING..       ")
        print("        A Gamified Task Prioritizer      ")
        print("=========================================")
        print(" 1. Quest Log")
        print(" 2. Add Quest")
        print(" 3. Complete Quest")
        print(" 4. Edit/Delete Quest")
        print(" 5. View Stats")
        print(" 6. Save & Exit")
        print("=========================================")
        
        ch = input("Enter Command: ")

        if ch == '1':
            while True:
                clear_screen()
                print("=== QUEST LOG ===")
                print("[1] View All Quests")
                print("[2] View Sorted Quests by Deadline")
                print("[3] View Sorted Quests by Difficulty")
                print("[4] Back to Main Menu")
                print("=================")
                ch2 = input("Enter Command: ")

                if ch2 == '1':
                    clear_screen()
                    print("--- ALL CURRENT QUESTS ---")
                    quest_log.view_quests()
                    input("\nPress [Enter] to go back...")
                elif ch2 == '2':
                    clear_screen()
                    print("--- SORTED BY DEADLINE ---")
                    quest_log.sorting_deadline()
                    input("\nPress [Enter] to go back...")
                elif ch2 == '3':
                    clear_screen()
                    print("--- SORTED BY DIFFICULTY ---")
                    quest_log.sorting_difficulty()
                    input("\nPress [Enter] to go back...")
                elif ch2 == '4':
                    break
                else:
                    print("Invalid Choice... Try Again")
                    time.sleep(1.5)

        elif ch == '2':
            clear_screen()
            print("=== ADD NEW QUEST ===")
            name = input("Enter Quest Name: ").strip()
            if not name:
                print("Quest name cannot be empty!")
                time.sleep(1.5)
                continue
                
            deadline = input("Enter Deadline (YYYY-MM-DD): ")
            
            print("\nSelect Difficulty Tier:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - Boss")
            
            try:
                difficulty = int(input("Select Difficulty (1-4): "))
                if difficulty not in [1, 2, 3, 4]:
                    print("Out of range. Defaulting to 1 (Easy).")
                    difficulty = 1
            except ValueError:
                print("Invalid input format. Defaulting to 1 (Easy).")
                difficulty = 1
                
            quest_log.add_task(name, deadline, difficulty)
            time.sleep(2)

        elif ch == '3':
            clear_screen()
            print("=== COMPLETE A QUEST ===")
            if not quest_log.container:
                print("No quests available to complete!")
            else:

                quest_log.view_quests()
                target_name = input("\nEnter the exact Quest Name to complete: ").strip()
                
                if target_name in quest_log.container:

                    diff_tier = quest_log.container[target_name]["Difficulty"]
                    xp_gained = int(diff_tier) * 50
                    
                    player_profile["XP"] += xp_gained
                    player_profile["Completed_Quests"].append(target_name)
                    
                    if player_profile["XP"] >= (player_profile["Level"] * 100):
                        player_profile["Level"] += 1
                        print(f"\n✨ LEVEL UP! You are now Level {player_profile['Level']}! ✨")
                    
                    quest_log.remove(target_name)
                    print(f"\nSuccessfully vanquished '{target_name}'!")
                    print(f"Gained +{xp_gained} XP!")
                else:
                    print("Quest title not found in logs.")
            input("\nPress [Enter] To Continue...")

        elif ch == '4':
            clear_screen()
            print("=== EDIT / DELETE QUEST ===")
            if not quest_log.container:
                print("No quests found to modify.")
                time.sleep(1.5)
                continue
                
            quest_log.view_quests()
            target_name = input("\nEnter Quest Name to edit/delete: ").strip()
            
            if target_name in quest_log.container:
                print("\n[1] Edit Title")
                print("[2] Edit Deadline")
                print("[3] Edit Difficulty")
                print("[4] Delete Quest")
                action = input("Select choice: ")
                
                if action == '1':
                    new_name = input("Enter new quest title: ").strip()
                    if new_name and new_name not in quest_log.container:
                        quest_log.container[new_name] = quest_log.container.pop(target_name)
                        print("Title updated successfully!")
                    else:
                        print("Invalid title or title already exists.")
                elif action == '2':
                    new_date = input("Enter new date (YYYY-MM-DD): ")
                    quest_log.container[target_name]["Deadline"] = new_date
                    print("Deadline updated successfully!")
                elif action == '3':
                    try:
                        new_diff = int(input("Enter new difficulty tier (1-4): "))
                        quest_log.container[target_name]["Difficulty"] = new_diff
                        print("Difficulty updated successfully!")
                    except ValueError:
                        print("Invalid integer entry.")
                elif action == '4':
                    quest_log.remove(target_name)
                else:
                    print("Invalid option selected.")
            else:
                print("That quest does not exist.")
            time.sleep(2)

        elif ch == '5':
            clear_screen()
            print("=========================================")
            print("         HERO PROFILE & STATISTICS       ")
            print("=========================================")
            print(f" Player Level : {player_profile['Level']}")
            print(f" Current Experience : {player_profile['XP']} XP")
            print(f" Next Level Up Goal : {player_profile['Level'] * 100} XP")
            print("=========================================")
            print(f" Completed Quests Log ({len(player_profile['Completed_Quests'])} items):")
            if not player_profile['Completed_Quests']:
                print("  - No completed achievements recorded yet.")
            else:
                for q in player_profile['Completed_Quests']:
                    print(f"  [✔] {q}")
            input("\nPress [Enter] to return to the Main Menu...")

        elif ch == '6':
            clear_screen()
            print("Thank you for playing StudyQuest!")
            print("Your adventure will continue next time.")
            time.sleep(2)
            break

        else:
            print("Invalid Choice! Please enter numbers 1 through 6.")
            time.sleep(1.5)
