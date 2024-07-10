def safe_divide(numerator, denominator):
    try:
        # Attempt to convert arguments to floats
        numerator = float(numerator)
        denominator = float(denominator)
        # Perform division (raises ZeroDivisionError if denominator is zero)
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    except ValueError:
        #Handle non-numeric input
        return "Please enter numeric values only."