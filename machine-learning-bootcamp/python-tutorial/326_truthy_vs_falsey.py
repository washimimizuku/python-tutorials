from decimal import Decimal
from fractions import Fraction


username = 'name'
password = 'password'

if username and password:
    print('You exist!')
else:
    print('Who are you?')


# Falsy
print(bool(None))

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(Decimal(0)))
print(bool(Fraction(0,1)))

print(bool([])) # Empty list
print(bool({})) # Empty dict
print(bool(())) # Empty tuple
print(bool('')) # Empty string
print(bool(b'')) # Empty bytes
print(bool(set())) # Empty set
print(bool(range(0)))
