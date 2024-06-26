task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Process the task based on priority and time sensitivity using Match Case
match priority:
    case 'high':
        message = f"'{task}' is a high priority task"
    case 'medium':
        message = f"'{task}' is a medium priority task"
    case 'low':
        message = f"'{task}' is a low priority task"
    case _:
        message = "Invalid priority input."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print(f"Reminder: {message}")
