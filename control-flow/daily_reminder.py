task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case 'low':
        reminder = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority input."

print("Reminder: ", reminder)
