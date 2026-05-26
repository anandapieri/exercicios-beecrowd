while True:
    try:
        palavra = input()
        [print(letra + ' ', end='') for letra in palavra[:-1]]
        print(palavra[-1], end='')
        print()

        for _ in range(len(palavra)-1):
            palavra = palavra[:-1]
            [print(letra + ' ', end='') for letra in palavra[:-1]]
            print(palavra[-1], end='')
            print()
        print()
    except EOFError:
        break