name = "Bob"
greeting = f"Hello, {name}!"

print(greeting)

name = "Rolf"

print(greeting)

print("###############################")

name = "Bob"

print(f"Hello, {name}!")

name = "Rolf"

print(f"Hello, {name}!")

print("###############################")

name = "Bob"
greeting = "Hello, {}!"
greeting_with_name = greeting.format(name)
greeting_with_name_two = greeting.format("Rolf")
print(greeting_with_name)
print(greeting_with_name_two)

print("###############################")

longer_phrase = "Hello, {}. Today is {}."
formatted_longer_phrase = longer_phrase.format("Rolf", "Monday")

print(formatted_longer_phrase)

