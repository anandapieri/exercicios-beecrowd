while True:
    try:
        N = int(input())

        codigos = []
        for _ in range(N):
            codigo = input()
            codigos.append(codigo)

        codigos.sort()
        [print(numero) for numero in codigos]
    
    except EOFError:
        break