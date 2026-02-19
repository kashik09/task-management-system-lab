# Import validation functions
from task_manager.validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    try:
        validate_task_title(title)
    except ValueError:
        print("Invalid task title.")
        return False

    try:
        validate_task_description(description)
    except ValueError:
        print("Invalid task description.")
        return False

    try:
        validate_due_date(due_date)
    except ValueError:
        print("Invalid due date. Use YYYY-MM-DD format.")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int) or index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return False

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task.get("completed", False)]
    if len(pending_tasks) == 0:
        print("No pending tasks.")
        return []

    for idx, task in enumerate(pending_tasks, start=1):
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")

    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0

    completed_tasks = sum(1 for task in tasks if task.get("completed", False))
    progress = (completed_tasks / len(tasks)) * 100
    return progress
