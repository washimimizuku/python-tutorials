my_list = [1, 2, 3, 4, 5, 6, 7]

def is_odd(item):
    return item % 2 != 0

new_list = list(filter(is_odd, my_list))

print(my_list)
print(new_list)
