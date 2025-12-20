basket = ['a', 'b', 'c', 'd', 'e', 'd']

print(basket)

print(basket.index('d'))
print(basket.index('d', 0, 4)) # Gives "ValueError: 'd' is not in list" if not found

print('d' in basket)
print('x' in basket)

print('i' in 'My name is Nuno')

print(basket.count('d'))
