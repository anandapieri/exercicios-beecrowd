def calcular_hash(L: int):
    hash = 0
    for i in range(L):
        palavra = input()

        for j, letra in enumerate(palavra):
            hash += i + j + (ord(letra) - ord('A'))
    return hash

N = int(input())
for _ in range(N):
    L = int(input())
    print(calcular_hash(L))