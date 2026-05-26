X = input()

vetor = [int(N) for N in input().split()]

for indice, valor in enumerate(vetor):
    if valor == min(vetor):
        print(f'Menor valor: {valor}')
        print(f'Posicao: {indice}')
