def calcular_hash(L: int):
    palavras = []
    i = 0
    while i < L:
        palavra = input()
        palavras.append(palavra)
        i+=1

    hash = 0
    hash_final = 0
    for j, palavra in enumerate(palavras):
        for k, letra in enumerate(palavra):
            hash += j + k + (ord(letra) - ord('A'))
    hash_final+=hash
    return hash_final

N = int(input())
for _ in range(N):
    L = int(input())
    numero_hash = calcular_hash(L)
    print(numero_hash)