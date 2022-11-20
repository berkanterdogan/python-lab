t = 5, 11  # (5, 11)
x, y = t

print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# Destructuring of student_attendance items
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

print(list(student_attendance.items()))

print("\n###############################\n")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(person)
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

print("\n###############################\n")

person = ("Bob", 42, "Mechanic")
# Underscore is so bad a variable name, but Python community has decided that if you use an underscore variable name,
# you don't care about this variable.
name, _, profession = person
print(name, profession)

print("\n###############################\n")

l = [1, 2, 3, 4, 5]
head, *tail = l
print(head)
print(tail)

first, second, *tail = l
print(head)
print(second)
print(tail)

*head, tail = l
print(head)
print(tail)
