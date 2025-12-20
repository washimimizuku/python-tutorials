my_set = {1, 2, 3, 4, 5, 5}

print(my_set)

my_set.add(100)
my_set.add(2)

print(my_set)

print(1 in my_set)
print(len(my_set))

print(list(my_set))

new_set = my_set.copy()
my_set.clear()

print(my_set)
print(new_set)

# Convert list to set (remove duplicates)
my_list = [1, 2, 3, 4, 5, 4, 3, 2]

print(set(my_list))
