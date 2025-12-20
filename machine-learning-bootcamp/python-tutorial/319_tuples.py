# Tuple: Immutable lists
my_tuple = (1, 2, 3, 4, 5)

# my_tuple[1] = 6 # Throws TypeError

print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    'basket': [1, 2, 3],
    'greeting': 'hello',
    'age': 20,
}

print(user.items()) # Returns a tuple

user = {
    (1, 2): [1, 2, 3],
    'greeting': 'hello',
    'age': 20,
}

print(user[(1, 2)])
