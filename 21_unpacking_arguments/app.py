def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 3, 5, 7))

print("\n###############################\n")


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(*nums)
print(add(**nums))

print("\n###############################\n")


def apply(*args, operator):
    print(args)
    print(*args)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 5, 7, operator="*"))
print(apply(1, 3, 5, 7, operator="+"))
