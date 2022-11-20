# We can modify lists(add, remove)
my_list = ["Bob", "Rolf", "Anne"]
my_list[0] = "Smith"
my_list.append("John")
print(my_list)
my_list.remove("Rolf")
print(my_list)

# We cannot modify tuples
my_tuple = ("Bob", "Rolf", "Anne")

# We can modify sets. We cannot have duplicate elements in sets. Also, sets don't guaranteed to keep order of elements.
my_set = {"Bob", "Rolf", "Anne"}
my_set.add("John")
my_set.add("John")
print(my_set)
my_set.remove("Rolf")
print(my_set)
