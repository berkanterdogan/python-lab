numbers = [1, 3, 5]

# doubled = []
# for x in numbers:
#     doubled.append(x * 2)

doubled = [x * 2 for x in numbers]  # New list is created.
print(doubled)

print("\n###############################\n")

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# starts_s = []
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

starts_s = [friend for friend in friends if friend.startswith("S")]  # New list is created.
print(starts_s)


friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # New list is created.
print("starts_s:", starts_s)
print("friends:", friends)
print(f"Result of 'friends is starts_s' is {friends is starts_s}")
print(f"Result of friends == starts_s is {friends == starts_s}")
print(f"id of friends:", id(friends), ", id of starts_s:", id(starts_s))  # memory addresses of the lists
print(f"Result of friends[0] is starts_s[0] is {friends[0] is starts_s[0]}")
