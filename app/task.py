import os
import json

last_id = 0
tasks = []

JSON_FILE = 'task.json'

def load_tasks():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    
    return []


def find_task_by_id(tasks: list, task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    return None


def save_tasks(tasks: list):
    with open(JSON_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def get_next_id(tasks):
    if tasks:
        last_id = max(task['id'] for task in tasks)
        return last_id + 1
    return 1


# Function to add a task 
def add_task(tasks: list, task: dict):
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")
    
    
# Function to remove a task
def remove_task(tasks):
    task_id = int(input("Enter the ID of the task to remove: "))
    task_to_remove = find_task_by_id(tasks, task_id)

    if task_to_remove:
        tasks.remove(task_to_remove)
        save_tasks(tasks)
        print(f"Task removed: {task_to_remove}")
    else:
        print("Task not found.")
        
        
# Function to alter a task's status      
def alter_task(tasks):
    task_id = int(input("Enter the ID of the task to alter: "))
    task_to_alter = find_task_by_id(tasks, task_id)
    
    if task_to_alter:
        new_status = input("Enter the new status for the task: ")
        task_to_alter["status"] = new_status
        save_tasks(tasks)
        print(f"Task ID {task_id} updated. New status: {new_status}")
    else:
        print("Task not found.")

# Function to list all tasks      
def list_tasks(tasks):
    if tasks:
        print(json.dumps(tasks, indent=2))
    else:
        print("Task list empty\n")


# Function to create a task
def create_task(tasks):
    new_id = get_next_id(tasks)
    task = {
        "id": new_id,
        "description": input("Please provide the task description: "),
        "status": input("Please provide the current status of the task: ")
    }
    
    return task


# A simple function to show a menu on the terminal and return the choosed option
def menu():
    print("Welcome! please choose a option")
    print("1 -- Add task")
    print("2 -- Remove task")
    print("3 -- Alter task")
    print("4 -- List all tasks")
    print("5 -- Exit")
    
    return input("Choose a option: ")
    
    
# Main function of the app   
def main():
    tasks = load_tasks()
    while True:
        option = menu()
        print()
        
        match option:
            case '1':
                task = create_task(tasks)
                add_task(tasks, task)
                print()
            
            case '2':
               remove_task(tasks)
                    
            case '3':
                alter_task(tasks)
            
            case '4':
                list_tasks(tasks)
            
            case '5':
                break
            
            case "_":
                print("Invalid option. Please try again. ")
            
if __name__ == "__main__":
    main()
