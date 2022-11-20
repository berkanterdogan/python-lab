from operator import itemgetter


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot ")

    return dividend / divisor


def calculate(*values, operator):
    print(values)
    print(*values)
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)

print("\n###############################\n")


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf", "age": 30},
    {"name": "Adam", "age": 35},
    {"name": "Anne", "age": 40},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Adam", get_friend_name))
print(search(friends, "Adam", lambda friend: friend["name"]))
print(search(friends, "Adam", itemgetter("name")))
