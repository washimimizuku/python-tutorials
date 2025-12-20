# Keys must be immutable and unique
user = {
    'basket': [1, 2, 3],
    'greeting': 'hello',
}

print(user)
print(user['greeting'])

# print(user['age']) # Would throw a KeyError
print(user.get('age'))
print(user.get('age', 55))

user2 = dict(name='JohnJohn', age=20)

print(user2)
print(user2.get('greeting'))
print(user2.get('age', 55))
