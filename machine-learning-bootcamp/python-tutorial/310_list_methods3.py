basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket)

print(sorted(basket)) # Does not modify basket

print(basket)

new_basket = basket.copy()

new_basket.sort() # Modifies basket
print(basket)
print(new_basket)

basket.reverse()
print(basket)

basket.sort()
basket.reverse()
print(basket)
