def calcular_anos(pop_a, pop_b, taxa_a, taxa_b):
    anos = 0
    while pop_a <= pop_b:
        pop_a += pop_a * (taxa_a / 100)
        pop_b += pop_b * (taxa_b / 100)
        anos += 1
    return anos

T = int(input())
anos = []

for _ in range(T):
    dados = input().split()
    pop_a = int(dados[0])
    pop_b = int(dados[1])
    taxa_a = float(dados[2])
    taxa_b = float(dados[3])
    X = calcular_anos(pop_a, pop_b, taxa_a, taxa_b)
    if X > 100:
        anos.append(X)
        break
    else:
        anos.append(X)

for numero in anos:
    if numero <= 100:
        print(f'{numero} anos.')
    else:
        print('Mais de 1 seculo.')