import sys


class Book:
    def __init__(self, name, author, isbn, year):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.year = int(year)

    def __str__(self):
        return f"{self.name}/{self.author}/{self.isbn}/{self.year}"


def load_library(file_path):
    books = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split("/")
                if len(parts) == 4:
                    books.append(Book(*parts))
    except FileNotFoundError:
        print(f"There is no '{file_path}', starting a new one.")
    return books


def save_books(file_path, books):
    with open(file_path, "w") as file:
        for book in sorted(books, key=lambda b: b.year):
            file.write(f"{book}\n")


def show_books(books):
    if not books:
        print("\nNo books yet, lets add one!")
        return

    print("\nCurrent Books:")
    for book in sorted(books, key=lambda b: b.year):
        print(f"{book.name} by {book.author}, {book.year} (ISBN: {book.isbn})")
    print()


def add_book():
    print("\nAdd a new book:")
    name = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    year = input("Year: ").strip()

    if name and author and isbn and year.isdigit():
        return Book(name, author, isbn, year)
    else:
        print("Please enter all required infos")
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python library.py <library.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    books = load_library(file_path)

    while True:
        print("\n1) Add Book  2) Show Library  Q) Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == '1':
            book = add_book()
            if book:
                books.append(book)
                save_books(file_path, books)
                print("Book added!")
        elif choice == '2':
            show_books(books)
        elif choice == 'q':
            print("See you again")
            break
        else:
            print("Try again")


if __name__ == "__main__":
    main()
