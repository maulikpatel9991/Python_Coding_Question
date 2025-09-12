"""
implement a simple console-based Library Management System in Python. This system should allow a user to:

Add books to the library
View all available books
Borrow books
Return borrowed books
Exit the system

"""


class Library:
    def __init__(self, books):
        self.available_books_list = books.copy()
        self.borrowed_books = []

    def available_books(self):
        if self.available_books_list:
            print("\nAvailable Books:")
            for book in self.available_books_list:
                print(f"- {book}")
        else:
            print("\nNo books are currently available.")

    def add_book(self):
        book_name = input("Enter the book name to add: ").strip()
        if not book_name:
            print("Book name cannot be empty.")
            return
        self.available_books_list.append(book_name)
        print(f"'{book_name}' has been added to the library.")

    def borrow_book(self):
        while True:
            book_name = input("Enter the book name to borrow: ").strip()
            if not book_name:
                print("Book name cannot be empty.")
            elif book_name not in self.available_books_list:
                print(f"'{book_name}' is not available in the library.")
            else:
                self.available_books_list.remove(book_name)
                self.borrowed_books.append(book_name)
                print(f"You have borrowed '{book_name}'.")

            more = input("Do you want to borrow another book? (yes/no): ").strip().lower()
            if more not in ['yes', 'y']:
                break

    def return_book(self):
        book_name = input("Enter the book name to return: ").strip()
        if not book_name:
            print("Book name cannot be empty.")
        elif book_name not in self.borrowed_books:
            print(f"'{book_name}' was not borrowed.")
        else:
            self.borrowed_books.remove(book_name)
            self.available_books_list.append(book_name)
            print(f"'{book_name}' has been returned successfully.")

    def menu(self):
        options = {
            1: self.add_book,
            2: self.available_books,
            3: self.borrow_book,
            4: self.return_book,
            5: exit
        }

        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. Show Available Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")

            try:
                choice = int(input("Select an option (1-5): "))
                if choice in options:
                    options[choice]()
                else:
                    print("Invalid choice. Please select a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")

# Entry point
if __name__ == '__main__':
    initial_books = ["Maths", "C++", "Python"]
    library = Library(initial_books)
    library.menu()
