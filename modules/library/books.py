from persona import Author, Member
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Location:
    rack_number: int


@dataclass
class BookCopies:
    book_id: str
    rack_number: Location.rack_number
    is_checked_out: bool
    checkout_member: Member
    checkout_date



@dataclass
class Book:
    isbn: str
    title: str
    publication_date: str
    author: Author
    subject_category: List
    book_items: List[BookCopies]

    def __post_init__(self):
        datetime.strptime(self.publication_date, "%Y-%m-%d")

    def search_book(self, author=None, title=None, subject_category=None):
        return author in self.author or title in self.title or subject_category in self.subject_category


@dataclass
class
