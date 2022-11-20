friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne", "Jack"}

local_friends = friends.difference(abroad)
print(local_friends)

print("###############################")

friends = local_friends.union(abroad)
print(friends)

print("###############################")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
