from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad! So, Default parameters are evaluated when
        # the function is defined, not the function is called.
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
rolf = Student("Rolf")
print(bob.grades)  # [90]
print(rolf.grades)  # [90] !!!

bob = Student("Bob", [80, 98])
bob.take_exam(90)
rolf = Student("Rolf", [70, 100])
print(bob.grades)  # [80, 98, 90]
print(rolf.grades)  # [70, 100]

print("\n###############################\n")


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # This is a better way
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
rolf = Student("Rolf")
print(bob.grades)  # [90]
print(rolf.grades)  # []

bob = Student("Bob", [80, 98])
bob.take_exam(90)
rolf = Student("Rolf", [70, 100])
print(bob.grades)  # [80, 98, 90]
print(rolf.grades)  # [70, 100]
