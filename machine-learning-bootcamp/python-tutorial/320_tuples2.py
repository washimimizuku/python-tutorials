my_tuple = (1, 2, 3, 4, 5, 4)

new_tuple = my_tuple[1:2]
print(new_tuple)

new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = my_tuple

print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(3))
print(my_tuple.count(4))

print(my_tuple.index(4))

print(len(my_tuple))
