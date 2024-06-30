def main():
  """
  This function prompts the user for a size and draws a square pattern with asterisks.
  """
  # Get user input for pattern size
  while True:
    try:
      size = int(input("Enter the size of the pattern (positive integer): "))
      if size > 0:
        break
      else:
        print("Invalid input. Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a positive integer.")

  # Draw the pattern using nested loops
  for i in range(size):
    for j in range(size):
      print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row
