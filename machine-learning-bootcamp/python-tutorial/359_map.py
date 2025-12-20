my_list = [1, 2, 3]

def multiply_by2(item):
    return item * 2

new_list = list(map(multiply_by2, my_list))

print(my_list)
print(new_list)
