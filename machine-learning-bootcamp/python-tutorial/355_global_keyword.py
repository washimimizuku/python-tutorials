a = 10 # Global

def confusion(b):
    print(b)
    a = 90 # Local
    print(a)

confusion(300)
print(a)

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count())

# Better not use global
total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total))))
