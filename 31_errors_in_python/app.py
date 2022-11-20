def divide(dividend, divisor):
    return dividend / divisor


def my_divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


# grades = [78, 99, 85, 100]
grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")

print()

grades = [70, 90, 100]
# grades = []
try:
    average = my_divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")


print("\n###############################\n")

students = [
    {"name": "Bob", "grades": [70, 80]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [95, 100]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = my_divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades! ", e)
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
