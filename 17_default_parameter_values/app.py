def add(x, y=7):
    print(x + y)


add(5 + 10)
add(5)

print("\n###############################\n")

default_y = 3


def add2(x, y=default_y):
    my_sum = x + y
    print(my_sum)


add2(5)  # 8
default_y = 10
add2(5)  # 8
