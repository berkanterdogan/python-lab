def add(x, y):
    return x + y


print(add(10, 7))

print("\n###############################\n")

add2 = lambda x, y: x + y

print(add2(2, 3))
print((lambda x, y: x + y)(2, 3))

print("\n###############################\n")


def double(x):
    return x * 2


sequence = [1, 3, 5, 7]
doubled = [x * 2 for x in sequence]
print(doubled)

doubled = [double(x) for x in sequence]
print(doubled)

doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)

doubled = list(map(double, sequence))
print(doubled)

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
