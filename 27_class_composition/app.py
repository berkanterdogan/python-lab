class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


b1 = Book("B1")
b2 = Book("B2")
b3 = Book("B3")
shelf = BookShelf(b1, b2, b3)

print(shelf)
