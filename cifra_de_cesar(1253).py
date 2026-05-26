N = int(input())

for _ in range(N):
    palavra = input()
    posicao = int(input())

    cifra = ''
    for caracter in palavra:
        codigo = ord('A') + (ord(caracter) - ord('A') - posicao) % 26
        cifra += chr(codigo)

    print(cifra)

'''base = ord('A')

for caracter in palavra:
    valor = ord(caracter) - base
    novo_valor = (valor - posicao) % 26
    cifra += chr(base + novo_valor)'''