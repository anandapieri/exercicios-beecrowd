primeiro_caso = True

while True:
    N = int(input())

    if N == 0:
        break

    if not primeiro_caso:
        print()

    primeiro_caso = False

    palavras = [input() for palavra in range(N)]
    maior_tamanho = max(len(palavra) for palavra in palavras)
    for palavra in palavras:
        tamanho_palavra = len(palavra)
        espaco = maior_tamanho - tamanho_palavra
        print(espaco * ' ' + palavra)