for x in range(1,10):
    if x % 2 == 0:
        print(f'{x} is even')
    elif x % 3 == 0:
        print(f'{x} is odd')
    elif x % 2 != 0 or x % 3 != 0:
        print(f'{x} in not divisible')
        