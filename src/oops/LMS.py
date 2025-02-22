class Book:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Book Name  {self.name}, Book Author {self.author}, Book ISBN code {self.isbn}")


class Library:
    def __init__(self):
        self.books_list = []

    def add_book(self, book):
        if book is not None:
            self.books_list.append(book)

    def remove_book(self, isbn):
        book_to_delete = None
        for book in self.books_list:
            if book.isbn == isbn:
                book_to_delete = book

        if book_to_delete is not None:
            self.books_list.remove(book_to_delete)

    def print_books(self):
        for book in self.books_list:
            book.display()



first_book = Book("Bjarne", "c++", 1234)
second_book = Book('Herbs', "c++", 5678)
library = Library()
library.add_book(first_book)
library.add_book(second_book)

library.remove_book(1234)
third_book = Book('Scott', "c++", 15678)

library.add_book(third_book)
library.print_books()
