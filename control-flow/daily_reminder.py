def main():
  """
  This function gets user input about a task and provides a reminder.
  """
  # Get user input for task
  task = input("Enter your task: ")

  # Get user input for priority
  priority = input("Priority (high/medium/low): ").lower()

  # Get user input for time sensitivity
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Process task based on priority and time sensitivity
  reminder_message = match priority:
  case "high":
  if time_bound == "yes":
    return f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
  else:
    return f"Reminder: '{task}' is a high priority task. Complete it when possible."
  case "medium":
  return f"Reminder: '{task}' is a medium priority task. Consider completing it when you have time."
case "low":
return f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
case _:
return "Invalid priority level. Please enter high, medium, or low."
# Print the reminder message
print (f"print reminder:(This project requires immediate attention)")