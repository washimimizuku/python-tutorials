my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_list = [char for char in 'hello']

print(my_list)

my_list = [num for num in range(0, 100)]

print(my_list)

my_list = [num * 2 for num in range(0, 100)]

print(my_list)

my_list = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
