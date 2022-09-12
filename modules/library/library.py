"""

We will focus on the following set of requirements while designing the Library Management System:

Any library member should be able to search books by their title, author, subject category as well by the publication date.

Each book will have a unique identification number and other details including a rack number which will help to physically locate the book.

There could be more than one copy of a book, and library members should be able to check-out and reserve any copy. We will call each copy of a book, a book item.

The system should be able to retrieve information like who took a particular book or what are the books checked-out by a specific library member.

There should be a maximum limit (5) on how many books a member can check-out.

There should be a maximum limit (10) on how many days a member can keep a book.

The system should be able to collect fines for books returned after the due date.

Members should be able to reserve books that are not currently available.

The system should be able to send notifications whenever the reserved books become available, as well as when the book is not returned within the due date.

Each book and member card will have a unique barcode. The system will be able to read barcodes from books and members’ library cards.
"""
from typing import List, Dict
from persona import *
from books import *


class Library:
    def __init__(self):
        self.authors: Dict[int, Author] = list()
        self.users: List[User] = list()
        self.books: List[Book] = dict()
        self.admins: List[Administrator] = list()

    def add_book(self, user: User, new_book: Book):
        if type(user) != Administrator:
            raise Exception("Only admins can add a book")
        if any(book for book in self.books if book.isbn == new_book.isbn):
            raise Exception(f"Book with {new_book.isbn} already exists")
        self.books.append(new_book)

    def remove_book(self, book_isbn):
        # remove book if exists
        self.books = [book for book in self.books if book_isbn != book]

    def search_book(self, search_query: SearchQuery):
        if search_query.book_title:
            return [
                book for book in self.books.values()
                if search_query.book_title in book.title or search_query.author_name in book.author or
                   search_query.subject_category in book.subject_category or
                   search_query.publication_date == book.publication_date
            ]


library = Library()
