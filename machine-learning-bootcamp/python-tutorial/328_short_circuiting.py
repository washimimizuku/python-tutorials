is_friend = True
is_user = True

# Both are evaluated
if is_friend and is_user:
    print('best friends forever')

# Only is_friend is evaluated
if is_friend or is_user:
    print('best friends forever')

is_friend = False
is_user = False

# Only is_friend is evaluated
if is_friend and is_user:
    print('best friends forever')

# Both are evaluated
if is_friend or is_user:
    print('best friends forever')

