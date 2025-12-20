total = 100 # Global scope

def some_func():
    total = 200 # Function scope
    print(total)

some_func()
print(total)

if True:
    x = 10 # Also global scope

print(x)
