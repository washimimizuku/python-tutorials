# Iterables: tuple, list, set
for item in (1, 2, 3):
    for x in ['a', 'b', 'c']:
        for y in {'x', 'y', 'z'}:
            print(item, x, y)

# Iterables: string
for item in 'Zero to Mastery':
    print(item)

# Iterables: dictionary
user = {
    'name': 'Golem',
    'age': 50006,
    'can_swim': False
}

for item in user:
    print(item) # Prints keys

for item in user.items():
    print(item) # Prints (key, value)

for item in user.keys():
    print(item) # Prints keys

for item in user.values():
    print(item) # Prints value

for key, value in user.items():
    print(key, value)
    