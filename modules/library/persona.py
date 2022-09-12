from library import Book
from search import SearchQuery
from dataclasses import dataclass
from abc import ABC
from typing import ClassVar, List
from library import library


@dataclass
class User(ABC):
    user_id: str
    name: str
    dob: str
    address: str

    def search_book(self, search_query: SearchQuery) -> Book:
        return library.books.search(search_query.book_title, search_query.author_name, search_query.subject_category)



@dataclass
class Member(User):
    book_limit: ClassVar[int] = 10
    current_books_checked_out: List[int]

    def checkout_book(self, book: Book):



class Administrator(User):
    def __init__(self, user_id, name, dob, address):
        super().__init__(user_id, name, dob, address)






class Author(User):
    pass
