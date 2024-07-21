class Calculator:
  """
  A class for performing basic calculations.
  """

  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Adds two numbers and returns the sum.

    This is a static method and does not require an instance or access class attributes.
    """
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Multiplies two numbers and returns the product.

    This is a class method and receives the class itself (cls) as the first argument.
    It can access class attributes like calculation_type.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b