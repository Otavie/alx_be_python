task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time == "yes":
            print(f"{task} is a medium priority task that should be completed soon.")
        else:
            print(f"{task} is a medium priority task. Schedule it for completion.")
    case "low":
        if time == "yes":
            print(f"{task} is a low priority task but has a deadline. Try to complete it on time.")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time")