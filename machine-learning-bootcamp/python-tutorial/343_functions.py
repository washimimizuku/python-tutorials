def say_hello():
    print('hellllooooo')

say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

def show_tree():
    fill = '*'
    empty = ' '

    for row in picture:
        for column in row:
            if column:
                print(fill, end='')
            else:
                print(empty, end='')
        print()

show_tree()
show_tree()
show_tree()

print(show_tree)
