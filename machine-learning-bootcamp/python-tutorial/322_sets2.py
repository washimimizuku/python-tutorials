my_set = {1, 2, 3, 4, 5, 6}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set)
print(your_set)

# Difference between sets
print(my_set.difference(your_set))
print(your_set.difference(my_set))

# Intersection between sets
print(my_set.intersection(your_set))
print(my_set & your_set)

# Do the sets intersect?
print(my_set.isdisjoint(your_set))

# Union of sets
print(my_set.union(your_set))
print(my_set | your_set)

# Is subset
print(my_set.issubset(your_set))

# Is superset
print(my_set.issuperset(your_set))

# Remove item by id
my_set.discard(6)
print(my_set)

# Remove items found in another set
my_set.difference_update(your_set)
print(my_set)
