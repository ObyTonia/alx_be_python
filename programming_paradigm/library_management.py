class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author
        self._is_checked_out= False # Initially, book is available
    def __str__(self):
       """Returns a string representation of the book."""
       return f"{self.title} by {self.author}"

class Library:
    """Represents a library with a collection of books."""
    def __init__(self):
        """Initializes a Library instance."""
        self._books = []  # Private list to store Book instance
    def add_book(self, book):
       """Adds a book to the library's collection."""
       self._books.append(book)
       
    def check_out_book(self, title):
       """Attempts to check out a book by title, marking it unavailable."""
       for book in self._books:
        if book.title == title and not book._is_checked_out:
            book._is_checked_out = True
            print(f"{title} has been checked out successfully.")
            return
        print(f"Sorry, '{title}' is not available for checkout.")
       
    def return_book(self, title):
        """Attempts to return a book by title, marking it available."""
        for book in self._books:
           if book.title == title and book._is_checked_out:
             book._is_checked_out = False
             print(f"{title} has been returned.")
             return
        print(f"Sorry, '{title}' is not currently checked out.")
       
    def list_available_books(self):
       """Prints a list of all available books in the library."""
       #print("Available Books:")
       for book in self._books:
          if not book._is_checked_out:
             print(f"- {book}") # Use book's __str__ method for formatted output
             
             #return
          #print("No books available in the library.")
            