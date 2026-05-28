while True:
    try:
        L = int(input())
        velocidade_maxima = max(list(map(int, input().split())))

        if velocidade_maxima < 10:
            print('1')
        elif velocidade_maxima >= 20:
            print('3')
        else:
            print('2')

    except EOFError:
        break
