def calcular_anos(pop_a, pop_b, taxa_a, taxa_b):
    anos = 0
    while pop_a <= pop_b and anos <= 100:
        pop_a += int(pop_a * (taxa_a / 100))
        pop_b += int(pop_b * (taxa_b / 100))
        anos += 1
    return anos

T = int(input())

for _ in range(T):
    dados = input().split()
    pop_a = int(dados[0])
    pop_b = int(dados[1])
    taxa_a = float(dados[2])
    taxa_b = float(dados[3])
    anos = calcular_anos(pop_a, pop_b, taxa_a, taxa_b)
    
    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')