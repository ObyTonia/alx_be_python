class Book:
  """
  Base class representing a book.
  """
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def __str__(self):
    return f""
class EBook(Book):
  """
  Derived class representing an electronic book.
  """
  def __init__(self, title, author, file_size):
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size  # Add EBook specific attribute

class PrintBook(Book):
  """
  Derived class representing a printed book.
  """
  def __init__(self, title, author, page_count):
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count  # Add PrintBook specific attribute

class Library:
  """
  Class representing a library managing a collection of books.
  """
  def __init__(self):
    self.books = []  # List to store Book objects

  def add_book(self, book):
    """
    Adds a Book instance to the library collection.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library.
    """
    for book in self.books:
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")
