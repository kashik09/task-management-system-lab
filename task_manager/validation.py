from datetime import datetime

def validate_task_title(title):
    title = str(title).strip()
    if len(title) == 0:
        raise ValueError("Title cannot be empty")
    return True

def validate_task_description(description):
    description = str(description).strip()
    if len(description) == 0:
        raise ValueError("Description cannot be empty")
    return True

def validate_due_date(due_date):
    due_date = str(due_date).strip()
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")
    datetime.strptime(due_date, "%Y-%m-%d")
    return True
