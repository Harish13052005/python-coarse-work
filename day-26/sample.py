from abc import ABC, abstractmethod

# -------------------- Abstraction --------------------
class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title              # Public
        self._author = author           # Protected
        self.__available = True         # Private

    @abstractmethod
    def display_info(self):
        pass

    # Encapsulation (Getter)
    def is_available(self):
        return self.__available

    # Encapsulation (Setter)
    def set_availability(self, status):
        self.__available = status


# -------------------- Inheritance --------------------
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    # Polymorphism
    def display_info(self):
        status = "Available" if self.is_available() else "Issued"
        print(f"\nBook : {self.title}")
        print(f"Author : {self._author}")
        print(f"Pages : {self.pages}")
        print(f"Status : {status}")


class Magazine(LibraryItem):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    # Polymorphism
    def display_info(self):
        status = "Available" if self.is_available() else "Issued"
        print(f"\nMagazine : {self.title}")
        print(f"Editor : {self._author}")
        print(f"Issue : {self.issue}")
        print(f"Status : {status}")


# -------------------- Library --------------------
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.title} added successfully.")

    def show_items(self):
        if not self.items:
            print("Library is empty.")
            return

        for item in self.items:
            item.display_info()

    def issue_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if item.is_available():
                    item.set_availability(False)
                    print(f"{title} issued successfully.")
                else:
                    print(f"{title} is already issued.")
                return
        print("Item not found.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if not item.is_available():
                    item.set_availability(True)
                    print(f"{title} returned successfully.")
                else:
                    print(f"{title} was not issued.")
                return
        print("Item not found.")


# -------------------- Main Program --------------------
library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Display Items")
    print("4. Issue Item")
    print("5. Return Item")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        pages = int(input("Pages: "))
        library.add_item(Book(title, author, pages))

    elif choice == "2":
        title = input("Magazine Title: ")
        editor = input("Editor: ")
        issue = input("Issue Number: ")
        library.add_item(Magazine(title, editor, issue))

    elif choice == "3":
        library.show_items()

    elif choice == "4":
        title = input("Enter title to issue: ")
        library.issue_item(title)

    elif choice == "5":
        title = input("Enter title to return: ")
        library.return_item(title)

    elif choice == "6":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")
