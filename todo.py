import sys

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def show_tasks(tasks):
    if not tasks:
        print("Your list is empty!")
    else:
        print("\n--- YOUR COMMAND LIST ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("-------------------------\n")

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        print("Usage: python todo.py [list | add <task> | remove <index>]")
        return

    action = sys.argv[1].lower()

    if action == "list":
        show_tasks(tasks)
    elif action == "add" and len(sys.argv) > 2:
        task = " ".join(sys.argv[2:])
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added: '{task}'")
    elif action == "remove" and len(sys.argv) > 2:
        try:
            idx = int(sys.argv[2]) - 1
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Removed: '{removed}'")
        except (ValueError, IndexError):
            print("Invalid task number.")

if __name__ == "__main__":
    main()
