def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total 

print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
print(super_func(1, 2, 3, 4, 5, 6, 7, 8, num1=5, num2=10, num3=50))

# Rule: parameters, *args, default parameters, **kwargs
def super_func(name, *args, greeting='Hi', **kwargs):
    total = sum(args)

    for items in kwargs.values():
        total += items

    print(f'{greeting} {name}, here is your total: {total}')

super_func('Nuno', 1, 2, 3, 4, 5, num1=5, num2=10)
