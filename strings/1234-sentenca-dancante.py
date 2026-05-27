while True:
    try:
        testes = input()

        i = 0
        for letra in testes:
            if letra.isalpha():
                if i % 2 == 0:
                    print(letra.upper(), end='')
                    i += 1
                else:
                    print(letra.lower(), end='')
                    i+=1
            else:
                print(letra, end='')
        print()
    except EOFError:
        break