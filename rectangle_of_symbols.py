for i in range(7):
    if i == 0 or i == 6:
        for j in range(20):
            print('0', end='')
    else:
        print('0', end='')
        for j in range(1, 19):
            print('1', end='')
        print('0', end='')
    print()
