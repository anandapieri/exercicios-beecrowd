def desembaralha_frase(frase: str):
    meio = len(frase) // 2
    metade_esquerda = (frase[:meio:])
    metade_direita = (frase[meio:])
    return metade_esquerda[::-1] + metade_direita[::-1]

N = int(input())

for _ in range(N):
    frase = input()
    print(desembaralha_frase(frase))