# Variable to control the auto-increment of the id
last_id = 0

# List to store dictionaries (simulating a database)
tasks = []


# Function to add a task 
def add_task(task): 
    tasks.append(task)
    print("Task added.")
    
    
# Function to remove a task
def remove_task():
    task_id = int(input("Enter the ID of the task to remove: "))
    
    task_to_remove = None
    for task in tasks:
        if task["id"] == task_id:
            task_to_remove = task
            break
    
    if task_to_remove:
        tasks.remove(task_to_remove)
        print(f"Task removed: {task_to_remove}")
    else:
        print("Task not found.")
        
        
# Function to alter a task's status      
def alter_task():
    task_id = int(input("Enter the ID of the task to alter: "))
    
    task_to_alter = None
    for task in tasks:
        if task["id"] == task_id:
            task_to_alter = task
            break
    
    if task_to_alter:
        new_status = input("Enter the new status for the task: ")
        task_to_alter["status"] = new_status
        print(f"Task ID {task_id} updated. New status: {new_status}")
    else:
        print("Task not found.")

# Function to list all tasks      
def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found.")


# Function to create a task
def create_task():
    global last_id
    last_id += 1
    
    task = {
        "id": last_id,
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
    while True:
        option = menu()
        print()
        
        match option:
            case '1':
                task = create_task()
                add_task(task)
                print()
            
            case '2':
               remove_task()
                    
            case '3':
                alter_task()
            
            case '4':
                list_tasks()
            
            case '5':
                break
            
            case "_":
                print("Invalid option. Please try again. ")
            
if __name__ == "__main__":
    main()
