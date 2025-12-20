# Scope rules
# 1 - Start with local
# 2 - Parent local
# 3 - Global
# 4 - Built-in Python

a = 1 # Global

def confusion():
    a = 5 # Local
    return a

print(a)
print(confusion())

def parent():
    a = 10 # Parent local
    def confusion():
        return a # Parent local
    return confusion()

print(a)
print(parent())

def my_sum(li):
    def sum(li):
        total = 0
        for number in li:
            total += number
        return total
    return sum(li) # Local sum()

print(my_sum([1, 2, 3]))

print(sum([1, 2, 3])) # Built-in Python sum()
