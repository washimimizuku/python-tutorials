def sum(num1, num2):
    return num1 + num2

print(sum(4, 5))
print(sum(10, 53))

total = sum(10, 5)

print(total)
print(sum(10, total))

def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum2(10, 5)

print(total)
