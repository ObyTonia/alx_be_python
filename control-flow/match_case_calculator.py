def main():
  """Prompts user for input and performs calculation."""
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Choose the operation (+, -, *, /): ")

def calculate(num1, num2, operator):
  """Performs the chosen operation using match-case."""
  match operator:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      if num2 == 0:
        return "Cannot divide by zero."
      else:
        return num1 / num2
    case _:
      return "Invalid operation."
    
    print(f"The result is {resul}")