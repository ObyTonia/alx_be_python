from datetime import datetime, timedelta
def display_current_datetime():
    """ Gets current date and time"""
current_date = datetime.now()
#Prints formatted Date and Time
print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date ():
    """This function calculates a future date by adding a specified number of days to the current date.
  Args:
      number_of_days (int): The number of days to add to the current date.
      """
number_of_days = int(input("Enter the number of days to add to the current date: "))
current_date = datetime.now()
future_date = current_date + timedelta(days=number_of_days)
print(f"Future date: {future_date.strftime('%Y-%m-%d')}")