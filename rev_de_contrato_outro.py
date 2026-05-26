while True:
    D, N = input().split()

    if D == "0" and N == "0":
        break

    # Remove o dígito D
    resultado = ''.join(c for c in N if c != D)

    # Remove zeros à esquerda
    resultado = resultado.lstrip('0')

    # Se ficou vazio, imprime 0
    if resultado == "":
        print("0")
    else:
        print(resultado)