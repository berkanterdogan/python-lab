student = {"name": "Rolf", "grades": (80, 84, 100, 98)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))

print("\n###############################\n")


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Rolf", (80, 84, 100, 98))
print(student.name)
print(student.grades)
print(student.average())
print(Student.average(student))
print(average(student.grades))

print("\n###############################\n")


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {
            'name': name,
            'price': price
        }
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = sum(item["price"] for item in self.items)
        return total


my_store = Store("My Store")
my_store.add_item("Book 1", 10)
my_store.add_item("Book 2", 25)

print(my_store.stock_price())
