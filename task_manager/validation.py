from datetime import datetime

def validate_task_title(title):
    cleaned_title = str(title).strip()
    while True:
        if len(cleaned_title) == 0:
            return False
        return True
    
def validate_task_description(description):
    cleaned_description = str(description).strip()
    while True:
        if len(cleaned_description) == 0:
            return False
        return True
    
def validate_due_date(due_date):
    cleaned_due_date = str(due_date).strip()
    while True:
        if len(cleaned_due_date) == 0:
            return False
        try:
            datetime.strptime(cleaned_due_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
