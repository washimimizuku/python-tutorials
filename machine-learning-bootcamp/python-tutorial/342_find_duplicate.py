some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
seen_list = []

for letter in some_list:
    if letter in seen_list:
        print(letter)
    else:
        seen_list.append(letter)

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
