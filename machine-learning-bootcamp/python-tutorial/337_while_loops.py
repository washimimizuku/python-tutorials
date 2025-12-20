i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done with all the work')

i = 0
while i < 50:
    print(i)
    i += 1
    break
else: # Not called because of break
    print('Done with all the work')
