def highest_even(li):
    highest = 0
    for number in li:
        if number % 2 == 0 and number > highest:
            highest = number
    return highest

print(highest_even([10, 2, 3, 4, 8, 11]))

def highest_even(li):
    evens = []
    for number in li:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))
