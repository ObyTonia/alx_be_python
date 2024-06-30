def main():
  """
  This function prompts the user for a number and prints its multiplication table.
  """
  # Get user input for number
  number = int(input("Enter a number to see its multiplication table: "))

  # Print multiplication table header
  print("Multiplication Table for", number)

  # Use for loop to iterate from 1 to 10
  for i in range(1, 11):
    # Calculate product and print the table row
    product = number * i
    print(f"{number} * {i} = {product}")