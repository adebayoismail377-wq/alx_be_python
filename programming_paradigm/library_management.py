# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Was not checked out

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a readable representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print all books that are available for checkout."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book_str in available_books:
                print(book_str)
        else:
            print("No books are currently available.")
