from datetime import datetime

def validate_task_title(title):
    title = str(title).strip()
    if(len(title)):
        return True
    raise ValueError("Title cannot be empty")

def validate_task_description(description):
    description = str(description).strip()
    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters")
    if(len(description)):
        return True
    raise ValueError("Description cannot be empty")

def validate_due_date(due_date):
    due_date = str(due_date).strip()
    if(len(due_date)):
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    raise ValueError("Due date cannot be empty")
