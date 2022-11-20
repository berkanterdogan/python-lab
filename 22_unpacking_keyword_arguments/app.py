def named(**kwargs):
    print(kwargs)


named(name="Bob", age=30)

print("\n###############################\n")


def named2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 30}

named(**details)
named2(**details)

print("\n###############################\n")


def print_nicely(**kwargs):
    named(**kwargs)
    count = 0
    for arg, value in kwargs.items():
        count +=1
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)

print("\n###############################\n")


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 4, 7, name="Bob", age=30)

