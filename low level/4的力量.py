user_input = int(input())

if user_input < 1:
    print(False)
else:
    while user_input % 4 == 0:
        user_input //= 4
    print(user_input == 1)