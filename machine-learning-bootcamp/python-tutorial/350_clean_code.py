# Complicated
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

# Better
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Even Better
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# Clean
def is_even(num):
    return num % 2 == 0

print(is_even(51))
print(is_even(52))
