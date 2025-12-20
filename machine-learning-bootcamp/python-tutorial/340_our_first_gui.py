picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    text = ''

    for column in row:
        if column:
            text += '*'
        else:
            text += ' '

    print(text)

for row in picture:
    for column in row:
        if column:
            print('*', end='')
        else:
            print(' ', end='')
    print()

fill = '*'
empty = ' '

for row in picture:
    for column in row:
        if column:
            print(fill, end='')
        else:
            print(empty, end='')
    print()
