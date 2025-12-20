my_list = [1, 2, 3]

for item in my_list:
    print(item)
    break # Breaks loop

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue # skips to next loop
    print('Not printed')

def some_function():
    pass # Does nothing
