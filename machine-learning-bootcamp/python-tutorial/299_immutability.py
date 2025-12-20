numbers = '01234567'
print(numbers)

numbers = '100'
print(numbers)

# Immutability

# This will not work
# numbers[0] = '8'

# This will create a new string
numbers = '01234567'
numbers = numbers + '8'

print(numbers)
