def say_hello(name='John Doe', emoji='😱'):
    print(f'hellllooooo {name} {emoji}')

# Positional arguments
say_hello('Nuno', '😁')
say_hello('Paula', '😁')
say_hello('Jasmine', '😁')

# Keyword arguments
say_hello(emoji='😁', name='Jasmine')
say_hello(name='Jasmine', emoji='😁')

# Default parameters
say_hello()
say_hello('Timmy')
say_hello(emoji='😁')
