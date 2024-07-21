class Book:
  """
  A class representing a book with title, author, and publication year.
  """

  def __init__(self, title, author, year):
    """
    Initializes a Book instance with the provided title, author, and year.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      year (int): The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints a message upon object deletion (not recommended for critical cleanup).

    This method is called by Python's garbage collector 
    when the object is no longer referenced.
    """
    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a string representation of the book in a human-readable format.

    This method is implicitly called when you print the object directly.
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string representation of the book suitable for recreating the object.

    This method is implicitly called when you use the `repr()` function on the object.
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"
