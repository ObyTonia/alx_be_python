import math

class Shape:
  """
  A base class representing a geometric shape.
  """

  def area(self):
    """
    This method is not implemented in the base class and raises an error.
    Derived classes need to override this method to calculate their specific area.
    """
    raise NotImplementedError("Area calculation not implemented for base Shape class")

class Rectangle(Shape):
  """
  A class representing a rectangle with length and width attributes.
  """

  def __init__(self, length, width):
    """
    Initializes a Rectangle instance with length and width.

    Args:
      length (float): The length of the rectangle.
      width (float): The width of the rectangle.
    """
    self.length = length
    self.width = width

  def area(self):
    """
    Calculates and returns the area of the rectangle (length x width).

    Overrides the base class area() method.
    """
    return self.length * self.width

class Circle(Shape):
  """
  A class representing a circle with radius attribute.
  """

  def __init__(self, radius):
    """
    Initializes a Circle instance with radius.

    Args:
      radius (float): The radius of the circle.
    """
    self.radius = radius

  def area(self):
    """
    Calculates and returns the area of the circle (pi x radius^2).

    Overrides the base class area() method.
    """
    return math.pi * self.radius** 2