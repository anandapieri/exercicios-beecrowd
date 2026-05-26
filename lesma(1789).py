while True:
    try:
        velocidades = []
        L = int(input())
        valores = input().split()

        i = 0
        while i < L:
            V = int(valores[i])
            velocidades.append(V)
            i+=1

        M = max(velocidades)
        if M < 10:
            print('1')
        elif M >= 20:
            print('3')
        else:
            print('2')

    except EOFError:
        break
