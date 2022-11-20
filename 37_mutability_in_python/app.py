# lists are mutable
a = []
b = a

print(id(a))
print(id(b))

a.append(45)

print(id(a))
print(id(b))

print(a)
print(b)

print("\n###############################\n")

# tuples are immutable
a = ()
b = a

print(id(a))
print(id(b))

a = a + (45,)

print(id(a))
print(id(b))

print(a)
print(b)

print("\n###############################\n")

# integers are immutable
a = 6543
b = 6543

print(id(a))
print(id(b))

a = 7777

print(id(a))
print(id(b))

print("\n###############################\n")

# strings are immutable
a = "hello"
b = a

print(id(a))
print(id(b))

a += " world!"

print(id(a))
print(id(b))

# tuples, strings, integer, floats, and booleans are immutable.

