class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()
test.instance_method()

ClassTest.instance_method(test)
ClassTest.class_method()

ClassTest.static_method()

print("\n###############################\n")


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover_book(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback_book(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book1 = Book.hardcover_book("Harry Potter", 1500)
print(book1)

book2 = Book.paperback_book("Phyton 101", 600)
print(book2)


print("\n###############################\n")

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        # f"{store.name}, total stock price: {store.stock_price()}"
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)  # returns a Store with name "Test - franchise"
Store.franchise(store2)  # returns a Store with name "Amazon - franchise"

print(Store.store_details(store))  # returns "Test, total stock price: 0"
print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"
