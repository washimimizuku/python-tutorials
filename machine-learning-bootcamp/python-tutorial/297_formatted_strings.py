name = 'Johnny'
age = 55

print(name)
print('Hi ' + name + '. You are ' + str(age) + ' years old.')

# Formatted Strings on Python 3
print(f'Hi {name}. You are {age} years old.')

# Formatted Strings on Python 2
print('Hi {}. You are {} years old.'.format(name, age))
print('Hi {1}. You are {0} years old.'.format(name, age))
print('Hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100))
