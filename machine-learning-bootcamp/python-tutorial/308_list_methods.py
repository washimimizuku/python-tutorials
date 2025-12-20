basket = [1, 2, 3, 4, 5, 4]

print(basket)
print(len(basket))

# Adding
basket.append(6)
print(basket)

basket.insert(4, 100)
print(basket)

basket.extend([200, 201])
print(basket)

# Removing
last_value = basket.pop()
print(last_value)
print(basket)

first_value = basket.pop(0)
print(first_value)
print(basket)

basket.remove(4)
print(basket)

basket.clear()
print(basket)
