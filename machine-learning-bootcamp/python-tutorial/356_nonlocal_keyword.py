def outer():
    x = 'local'
    def inner():
        nonlocal x # Refer to parent local
        x = 'nonlocal'
        print('inner: ', x)
    
    inner()
    print('outer: ', x)

outer()
