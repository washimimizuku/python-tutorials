user = {
    'basket': [1, 2, 3],
    'greeting': 'hello',
    'age': 20,
}

print(user)
print('basket' in user)
print('size' in user)

print('age' in user.keys())
print('hello' in user.values())

print(user.items()) # Returns a tuple

user2 = user.copy()
print(user2)

user.clear()
print(user)
print(user2)

print(user2.pop('age'))
print(user2)

print(user2.popitem()) # Pops "randomly" (the last one)
print(user2)

user.update({'age': 44})
print(user)
user.update({'age': 46})
print(user)
