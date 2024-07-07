#Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius (fahrenheit):
    """
    This function converts a temperature from Fahrenheit to Celsius
    Args:
        fahrenheit (float): The temperature in Fahrenheit.
    Returns:
        float: The temperature in celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit (celsius):
    """
    This function converts a temperature from Celsius to Fahrenheit
    Args:
        celsius (float): The temperature in Celsius.
    Returns:
        float: The temperature in Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main ():
    """Prompts the user for temperature and unit, performs conversion, and displays the result."""
    while True:
        try:
           temperature = float (input("Enter the temperature to convert: "))
           unit = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
           if unit == "F":
              converted_temperature = convert_to_celsius (temperature)
              converted_unit = "C"
           elif unit == "C":
            converted_temperature = convert_to_fahrenheit(temperature)
            converted_unit = "F"
           else:
              raise ValueError("Invalid temperature. Please enter a numeric value.")
           print(f"{temperature:.2f} degrees {unit} is equal to {converted_temperature:.2f} degrees {converted_unit}.")
           break  
        except ValueError as e:
           print(f"Error: {e}")
if __name__ == "__main__":
   main()