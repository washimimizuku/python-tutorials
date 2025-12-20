my_list = [1, 2, 3]

# With for loop
for item in my_list:
    print(item)

# With while loop
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('Say something: ')
    if response == 'bye':
        break
