while True:

    N = int(input())
    if N == 0:
        break

    C = input()

    i = 0
    for comando in C:
        if comando == 'D':
            i += 1
        elif comando == 'E':
            i -= 1
    
    if i % 4 == 1:
        print('L')
    elif i % 4 == 2:
        print('S')
    elif i % 4 == 3:
        print('O')
    else:
        print('N')