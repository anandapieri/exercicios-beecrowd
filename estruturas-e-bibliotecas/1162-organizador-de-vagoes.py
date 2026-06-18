N = int(input())
for _ in range(N):

    L = int(input())
    ordem_vagoes = list(map(int, input().split()))
    vagoes_ordenado = sorted(ordem_vagoes)

    contador = 0
    while True:
        for i in range(L-1):
            if ordem_vagoes[i] > ordem_vagoes[i+1]:
                ordem_vagoes[i], ordem_vagoes[i+1] = ordem_vagoes[i+1], ordem_vagoes[i]
                contador +=1

        if ordem_vagoes == vagoes_ordenado:
            print(f'Optimal train swapping takes {contador} swaps.')
            break