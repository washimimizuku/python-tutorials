my_set = {char for char in 'hello'}
print(my_set)

my_set = {num for num in range(0, 100)}
print(my_set)

my_set = {num * 2 for num in range(0, 100)}
print(my_set)

my_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_set)
