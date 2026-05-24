"""
This FIle is for the Data Structure that the system will use
"""
from datetime import datetime


#============================
# Implementing a Stack for Tasks
#=============================
class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    

#===============================
# Implementing a Queue for Tasks
#===============================
class queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    
    def is_empty(self):
        return len(self.items) == 0


#================================
# Implementing a Hash Table for Tasks With chaining
#================================
class Task_HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        hash_key = self.get_hash(key)
        for element in self.arr[hash_key]:
            if element[0] == key:
                return element[1]  # Return the value associated with the key
        
    
    def __setitem__(self, key, value):
        hash_key = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_key][idx] = (key, value)  # Update existing key
                found = True
                break
        if not found:
            self.arr[hash_key].append((key, value))  # Add new key-value pair
    
    def display(self):
        has_tasks = False
        for bucket in self.arr:
            for key, value in bucket:
                has_tasks = True
                if isinstance(value, dict):
                    name = value.get("Name", "Unknown")
                    difficulty = value.get("Difficulty", "N/A")
                    deadline = value.get("Deadline", "N/A")

                    if isinstance(deadline, datetime):
                        deadline_str = f"{deadline.year}-{deadline.month:02d}-{deadline.day:02d}"
                    else:
                        deadline_str = str(deadline)

                    print(f"Name: {name}, Difficulty: {difficulty}, Deadline: {deadline_str}")

        if not has_tasks:
            print("No Tasks are listed")
        

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        for idex, element in enumerate(self.arr[hash_key]):
            if element[0] == key:
                del self.arr[hash_key][idex]  # Remove the key-value pair
                return

    def __contains__(self, key):
        hash_key = self.get_hash(key)
        for element in self.arr[hash_key]:
            if element[0] == key:
                return True
        return False
    
    def to_dict(self):
        result = {}
        for bucket in self.arr:
            for key, value in bucket:
                result[key] = value
        return result

    #============================
    # SORTING ALGORITHM FOR TASKS
    #============================
    def sort_tasks(self, by="difficulty"):
        tasks = []
        for bucket in self.arr:
            for key, value in bucket:
                if isinstance(value, dict):
                    tasks.append(value)

        if by.lower() == "difficulty":
            tasks.sort(key=lambda x: x.get("Difficulty", 0))
        elif by.lower() == "deadline":
            tasks.sort(key=lambda x: x.get("Deadline", datetime.max))
        else:
            print("Invalid sort option. Use 'difficulty' or 'deadline'.")
            return

        # Print sorted tasks
        for task in tasks:
            name = task.get("Name", "Unknown")
            difficulty = task.get("Difficulty", "N/A")
            deadline = task.get("Deadline", "N/A")

            if isinstance(deadline, datetime):
                deadline_str = f"{deadline.year}-{deadline.month:02d}-{deadline.day:02d}"
            else:
                deadline_str = str(deadline)

            print(f"Name: {name}, Difficulty: {difficulty}, Deadline: {deadline_str}")


