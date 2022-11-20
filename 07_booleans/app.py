print(5 == 5)
print(10 != 10)
print(5 > 5)

print("###############################")

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)

print("###############################")

abroad = ["Bob", "Rolf"]

print(friends == abroad)
print(friends is abroad)

print("###############################")

friends = abroad
print(friends == abroad)
print(friends is abroad)