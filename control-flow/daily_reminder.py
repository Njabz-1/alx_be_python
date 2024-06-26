task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case 'high':
        if time_bound == 'yes':
            reminder = f"{task} is a high priority task that requires immediate attention today!"
        else:
            reminder = f"{task} is a high priority task. Consider completing it when you have free time."
    case 'medium':
        if time_bound == 'yes':
            reminder = f"{task} is a medium priority task that should be done soon."
        else:
            reminder = f"{task} is a medium priority task. Try to complete it when possible."
    case 'low':
        if time_bound == 'yes':
            reminder = f"{task} is a low priority task but is time-bound. Try to complete it today."
        else:
            reminder = f"{task} is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority input."

print("Reminder: ",reminder)
