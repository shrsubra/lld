from dataclasses import dataclass
from datetime import datetime


@dataclass
class SearchQuery:
    author_name: str
    book_title: str
    subject_category: str
    publication_date: str

    def __post_init__(self):
        datetime.strptime(self.publish_date, "%Y-%m-%d")
