task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task"
        # Additional logic here
    case 'low':
        reminder = f"Note: '{task}' is a low priority task"
        # Additional logic here
    case _:
        reminder = "Invalid priority input."

print(reminder)
