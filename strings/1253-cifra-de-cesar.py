N = int(input())

for _ in range(N):
    palavra = input()
    posicao = int(input())

    cifra = ''
    for caracter in palavra:
        codigo = ord('A') + (ord(caracter) - ord('A') - posicao) % 26
        cifra += chr(codigo)

    print(cifra)