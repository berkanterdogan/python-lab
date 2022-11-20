from typing import List  # , Tuple, Set, etc...


def list_avg2(sequence: List) -> float:
    return sum(sequence) / len(sequence)


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

    def __str__(self) -> str:
        return f"Book {self.name}"


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books


b1 = Book("B1", "100")
b2 = Book("B2", "120")

shelf = BookShelf([b1, b2])
