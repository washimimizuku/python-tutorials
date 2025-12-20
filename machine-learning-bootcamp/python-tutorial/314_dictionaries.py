dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': 3,
    'y': True,
}

print(dictionary)
print(dictionary['b'])
# print(dictionary['c']) # Would throw a KeyError

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': 3,
        'y': True,
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': 6,
        'y': True,
    },
    {
        'a': [7, 8, 9],
        'b': 'hello',
        'x': 9,
        'y': False,
    },
]

print(my_list)
print(my_list[2]['a'][1])
